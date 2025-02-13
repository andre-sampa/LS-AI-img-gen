# img_gen.py
import sys
import os
import random
from huggingface_hub import InferenceClient, login
from datetime import datetime
from config.config import prompts, api_token  
from config.models import models
from metadata.metadata import fetch_metadata

def generate_image(
        adventurer_id,
        prompt_alias, 
        custom_prompt, 
        characer_dropdown,
        model_alias, 
        height=360, 
        width=640, 
        num_inference_steps=20, 
        guidance_scale=2.0, 
        seed=-1):
    
    adventurer = fetch_metadata(adventurer_id)
    print(f"ANDRE {adventurer['name']}")

    # Set the custom prompt variables
    if characer_dropdown == "Portait":
        prompt = f"A portait of a medieval, fantasy adventurer, equiped with a weapon: a {adventurer['weapon']} (depending on his weapon, make the characer dressed as a warrior, or as a hunter or as a wizard). He is also equiped in the head with a {adventurer['head']}, the hands with {adventurer['hand']}, the chest with a {adventurer['chest']}, and the waist with a {adventurer['waist']}. Please be sure to use only medieval items that were possble to be made in that period. Unreal Engine render style, photorealistic, atmospheric light, realistic fantasy style."
    
    if characer_dropdown == "Last battle":
        prompt = f"A battle between a medieval fantasy adventurer, and a big {adventurer['beast']} monster. The adventurer is combating with {adventurer['weapon']} (depending on his equipment, make the characer dressed as a warrior, or as a hunter or as a wizard). He is also equiped in the head with {adventurer['head']}, the hands with {adventurer['hand']}, the chest with {adventurer['chest']}, the waist with {adventurer['waist']}, the fet with {adventurer['foot']}. Please sure to use only medieval items that were possble to be made in that period. Add details for the monster as well. is Unreal Engine render style, photorealistic, realistic fantasy style."

    elif characer_dropdown == "Loot bag":
        prompt = f"A loot bag from a medieval fantasy adventurer and his equipments. On the floor also a {adventurer['weapon']} a {adventurer['head']}, a {adventurer['hand']}, a {adventurer['chest']}, a {adventurer['waist']}, and a {adventurer['foot']}. Please sure to use only medieval items that were possble to be made in that period. Inside the bag also gold coins. Atmospheric light, cavern, dungeon context. Unreal Engine render style, photorealistic, realistic fantasy style."
    else:       
        pass



    # Find the selected prompt and model
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
    
    message = f"Image generated successfully! Call the banners! \nID: {adventurer['id']}, NAME: {adventurer['name']}, WEAPON: {adventurer['weapon']}, HEAD: {adventurer['head']}, HAND: {adventurer['hand']}, CHEST: {adventurer['chest']}, WAIST: {adventurer['waist']}, BEAST: {adventurer['beast']}"
    file_name_extension = f"ID: {adventurer['id']}, NAME: {adventurer['name']}, WEAPON: {adventurer['weapon']}, HEAD: {adventurer['head']}, HAND: {adventurer['hand']}, CHEST: {adventurer['chest']}, WAIST: {adventurer['waist']}, BEAST: {adventurer['beast']}"

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"{path}/{timestamp}_{seed}_{model_alias.replace(' ', '_').lower()}_{prompt_alias.replace(' ', '_').lower()}_{characer_dropdown.replace(' ', '_').lower()}_{file_name_extension.replace(' ', '_').lower()}.png"
    try:
        image.save(output_filename)
    except Exception as e:
        return None, f"ERROR: Failed to save image. Details: {e}"
    print("-----DONE!-----")
    print("-----CALL THE BANNERS!-----")

    return output_filename, message