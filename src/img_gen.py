# img_gen.py
import sys
import os
import random
from huggingface_hub import InferenceClient, login
from datetime import datetime
from config.config import models, prompts, api_token  # Direct import

def generate_image(
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
    try:
        prompt = next(p for p in prompts if p["alias"] == prompt_alias)["text"]
        model_name = next(m for m in models if m["alias"] == model_alias)["name"]

    except StopIteration:
        return None, "ERROR: Invalid prompt or model selected."

    # Print the original prompt and dynamic values for debugging
    print("Original Prompt:")
    print(prompt)

    # Append the custom character (if provided)
    if characer_dropdown == "Wizard":
        prompt += f" A wizard figths against the {prompt_alias}"
    elif characer_dropdown == "Warrior":
        prompt += f" A warrior figths against the {prompt_alias}"
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


    # Initialize the InferenceClient
    try:
        print("-----INITIALIZING INFERENCE-----")
        client = InferenceClient(model_name, token=api_token)
        print("Inference activated")
    except Exception as e:
        return None, f"ERROR: Failed to initialize InferenceClient. Details: {e}"

     #Generate the image
    try:
        print("-----GENERATING IMAGE-----")
        print("-----HOLD ON-----")   
        image = client.text_to_image(
            prompt,
            guidance_scale=guidance_scale,
            num_inference_steps=num_inference_steps,
            width=width,
            height=height,
            seed=seed
        )
        print("-----IMAGE GENERATED SUCCESSFULLY!-----")
    except Exception as e:
        return None, f"ERROR: Failed to generate image. Details: {e}"

    # Save the image with a timestamped filename
    print("-----SAVING-----", image)
    path = "images"
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"{path}/{timestamp}_{model_alias.replace(' ', '_').lower()}_{prompt_alias.replace(' ', '_').lower()}_{characer_dropdown.replace(' ', '_').lower()}.png"
    try:
        image.save(output_filename)
    except Exception as e:
        return None, f"ERROR: Failed to save image. Details: {e}"
    print("-----DONE!-----")
    print("-----CALL THE BANNERS!-----")

    return output_filename, "Image generated successfully!"