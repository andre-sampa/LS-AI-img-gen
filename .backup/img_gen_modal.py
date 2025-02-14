#img_gen_modal.py
import modal
import random
import io
from config.config import prompts, api_token 
from config.models import models_modal
import os
import gradio as gr
import torch
import sentencepiece
import torch
from huggingface_hub import login
from transformers import AutoTokenizer
import random
from datetime import datetime
from diffusers.callbacks import SDXLCFGCutoffCallback
from diffusers import FluxPipeline
from diffusers import DPMSolverMultistepScheduler, StableDiffusionPipeline, AutoencoderTiny, AutoencoderKL, DiffusionPipeline, FluxTransformer2DModel, GGUFQuantizationConfig
from PIL import Image
from src.check_dependecies import check_dependencies
import numpy as np

MAX_SEED = np.iinfo(np.int32).max
MAX_IMAGE_SIZE = 2048

CACHE_DIR = "/model_cache"

# Define the Modal image
image = (
    modal.Image.from_registry("nvidia/cuda:12.2.0-devel-ubuntu22.04", add_python="3.9")
                .pip_install_from_requirements("requirements.txt")
    #modal.Image.debian_slim(python_version="3.9")  # Base image
    # .apt_install(
    #     "git",
    # )
    # .pip_install(
    #     "diffusers",
    #     f"git+https://github.com/huggingface/transformers.git"
    # )
    .env(
        {
            "HF_HUB_ENABLE_HF_TRANSFER": "1", "HF_HOME": "HF_HOME", "HF_HUB_CACHE": CACHE_DIR
        }
    )
)

# Create a Modal app
app = modal.App("LS-img-gen-modal", image=image)
with image.imports():
    import os

flux_model_vol = modal.Volume.from_name("flux-model-vol", create_if_missing=True)  # Reference your volume

# GPU FUNCTION
@app.function(volumes={"/data": flux_model_vol},
              secrets=[modal.Secret.from_name("huggingface-token")],
              gpu="L40S",
              timeout = 300
              )
# MAIN GENERATE IMAGE FUNCTION
def generate_image_gpu(
        prompt_alias, 
        custom_prompt, 
        characer_dropdown,
        model_alias, 
        height=360, 
        width=640, 
        num_inference_steps=20, 
        guidance_scale=2.0, 
        seed=-1):
    # Find the selected prompt and model
    print("Hello from LS_img_gen!")

    check_dependencies()

    try:
        prompt = next(p for p in prompts if p["alias"] == prompt_alias)["text"]
        model_name = next(m for m in models_modal if m["alias"] == model_alias)["name"]

    except StopIteration:
        return None, "ERROR: Invalid prompt or model selected."

    # Print the original prompt and dynamic values for debugging
    print("Original Prompt:")
    print(prompt)

    # Append the custom character (if provided)
    if characer_dropdown == "Wizard":
        prompt += f" A wizard combats using powerful magic against the {prompt_alias}"
    elif characer_dropdown == "Warrior":
        prompt += f" A warrior combats using his weapons against the {prompt_alias}"
    else:
        pass

   # Append the custom prompt (if provided)
    if custom_prompt and len(custom_prompt.strip()) > 0:
        prompt += " " + custom_prompt.strip()

    # Print the formatted prompt for debugging
    print("\nFormatted Prompt:")
    print(prompt)

    # Randomize the seed if needed
    if seed == -1:
        seed = random.randint(0, 1000000)

    # HF LOGIN 
    print("Initializing HF TOKEN")
    print (api_token)
    # login(token=api_token)
    # print("model_name:")
    # print(model_name)


    # Use absolute path with leading slash
    model_path = f"/data/{model_name}"  # Changed from "data/" to "/data/"
    print(f"Loading model from local path: {model_path}")
    
    # Debug: Check if the directory exists and list its contents
    if os.path.exists(model_path):
        print("Directory exists. Contents:")
        for item in os.listdir(model_path):
            print(f" - {item}")
    else:
        print(f"Directory does not exist: {model_path}")
        print("Contents of /data:")
        print(os.listdir("/data"))
    # CHECK FOR TORCH USING CUDA
    print("CHECK FOR TORCH USING CUDA")
    print(f"CUDA available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print("inside if")
        print(f"CUDA device count: {torch.cuda.device_count()}")
        print(f"Current device: {torch.cuda.current_device()}")
        print(f"Device name: {torch.cuda.get_device_name(torch.cuda.current_device())}")

    try:
        print("-----INITIALIZING PIPE-----")
        pipe = FluxPipeline.from_pretrained(
            model_path,
            torch_dtype=torch.bfloat16,
            #torch_dtype=torch.float16,
            #torch_dtype=torch.float32,
            #vae=taef1,
            local_files_only=True,
        )
        #torch.cuda.empty_cache()

        if torch.cuda.is_available():
            print("CUDA available")
            print("using gpu")
            pipe = pipe.to("cuda")
            pipe_message = "CUDA"
            #pipe.enable_model_cpu_offload()  # official recommended method but is running slower w it
        else:
            print("CUDA not available")
            print("using cpu")
            pipe = pipe.to("cpu")
            pipe_message = "CPU"
        print(f"-----{pipe_message} PIPE INITIALIZED-----")
        print(f"Using device: {pipe.device}")
    except Exception as e:
        print(f"Detailed error: {str(e)}")
        return None, f"ERROR: Failed to initialize PIPE2. Details: {e}"

    ########## SENDING IMG GEN TO PIPE - WORKING CODE ##########
    try:
        print("-----SENDING IMG GEN TO PIPE-----")
        print("-----HOLD ON-----")   
        image = pipe(
            prompt,
            guidance_scale=guidance_scale,
            num_inference_steps=num_inference_steps,
            width=width,
            height=height,
            max_sequence_length=512,
            #callback_on_step_end=decode_tensors,
            #callback_on_step_end_tensor_inputs=["latents"],
            # seed=seed
        ).images[0]
        #############################################################

        print("-----IMAGE GENERATED SUCCESSFULLY!-----")
        print(image)  
                
    except Exception as e:
        return f"ERROR: Failed to initialize InferenceClient. Details: {e}"
        
    try:
        # Save the image with a timestamped filename
        print("-----SAVING-----", image)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"/data/LS_images/{timestamp}_{seed}_{model_alias.replace(' ', '_').lower()}_{prompt_alias.replace(' ', '_').lower()}_{characer_dropdown.replace(' ', '_').lower()}.png"
        try:
            image.save(output_filename)
        except Exception as e:
            return None, f"ERROR: Failed to save image. Details: {e}"
        print("-----DONE!-----")
        print("-----CALL THE BANNERS!-----")

    except Exception as e:
        print(f"ERROR: Failed to save image. Details: {e}")
    # Return the filename and success message
    return image, "Image generated successfully!"
