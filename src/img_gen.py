# img_gen.py
import sys
import os
import random
from huggingface_hub import InferenceClient, login
from datetime import datetime
from config.config import api_token  
from config.models import models
from metadata.metadata import fetch_metadata
from src.prompt_gen import prompt_gen


def generate_image(
        adventurer_id,
        #prompt_alias, 
        #character_dropdown,
        scene_dropdown,
        #model_alias,
        custom_prompt, 
        height=360, 
        width=640, 
        num_inference_steps=20, 
        guidance_scale=2.0, 
        seed=-1):
    
    print ("Sending to prompt gen")
    adventurer, prompt = prompt_gen(adventurer_id, scene_dropdown)

    id = adventurer['id']
    name = adventurer['name']
    weapon_equipment = adventurer['weapon']
    head_equipment = adventurer['head']
    hand_equipment = adventurer['hand']
    chest_equipment = adventurer['chest']
    waist_equipment = adventurer['waist']
    foot_equipment = adventurer['foot']
    gold_equipment = adventurer['gold']
    beast_last_battle = adventurer['beast']

    # Find the selected prompt and model
    model_alias = "FLUX.1-dev"
    try:
        #prompt = next(p for p in prompts if p["alias"] == prompt_alias)["text"]
        model_name = next(m for m in models if m["alias"] == model_alias)["name"]

    except StopIteration:
        return None, "ERROR: Invalid prompt or model selected."

    # Print the original prompt and dynamic values for debugging
    print("Original Prompt:")
    print(prompt)


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
    
    message = f"Image generated successfully! Call the banners! \n\n=====ADVENTURER GENERATED===== \nID: {id}\nNAME: {name}\nWEAPON: {weapon_equipment}\nHEAD: {head_equipment}\nHAND: {hand_equipment}\nCHEST: {chest_equipment}\nWAIST: {waist_equipment}\nFOOT: {foot_equipment}\nGOLD: {gold_equipment}\nLAST BATTLE BEAST: {beast_last_battle}"

    file_name_extension = f"{id}_{weapon_equipment}_{head_equipment}_{hand_equipment}_{chest_equipment}_{waist_equipment}_{foot_equipment}_{gold_equipment}_{beast_last_battle}"

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    output_filename = f"{path}/{timestamp}_{seed}_{model_alias.replace(' ', '_').lower()}_{scene_dropdown.replace(' ', '_').lower()}_{file_name_extension.replace(' ', '_').lower()}.png"
    
    # output_filename = f"{path}/{timestamp}_{seed}_{model_alias.replace(' ', '_').lower()}_{prompt_alias.replace(' ', '_').lower()}_{characer_dropdown.replace(' ', '_').lower()}_{file_name_extension.replace(' ', '_').lower()}.png"

    try:
        image.save(output_filename)
    except Exception as e:
        return None, f"ERROR: Failed to save image. Details: {e}"
    print("-----DONE!-----")
    print("-----CALL THE BANNERS!-----")

    return output_filename, message