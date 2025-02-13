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
        #prompt_alias, 
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

    id = adventurer['id']
    name = adventurer['name']
    weapon_equipment = adventurer['weapon']
    head_equipment = adventurer['head']
    hand_equipment = adventurer['hand']
    chest_equipment = adventurer['chest']
    waist_equipment = adventurer['waist']
    foot_equipment = adventurer['foot']
    beast_last_battle = adventurer['beast']

    # Set the custom prompt variables
    if characer_dropdown == "Portait":
        prompt = f"A portait of a medieval, fantasy adventurer, holding a {weapon_equipment} (depending on his weapon, make the characer dressed as a warrior, or as a hunter or as a wizard). He is also equiped in the head with a {head_equipment}, the hands with {hand_equipment}, the chest with a {chest_equipment}, and the waist with a {waist_equipment}. Please be sure to use only medieval items that were possble to be made in that period. Make the adventurer unshaved and dirty, he have been figthing for days down into the dungeons. Unreal Engine render style, photorealistic, atmospheric light, realistic fantasy style."
    
    if characer_dropdown == "Last battle":
        prompt = f"A battle between a medieval fantasy adventurer, and a massive {beast_last_battle} monster. The adventurer is holding a weapon: a {weapon_equipment}. He is also equiped in the head with {head_equipment}, the hands with {hand_equipment}, the chest with {chest_equipment}, the waist with {waist_equipment}, the fet with {foot_equipment}. Use only medieval items that were possble to be made in that period. Add details for the monster as well. The scene location is the natural ambient of the {beast_last_battle}. Unreal Engine render style, photorealistic, realistic fantasy style."

    elif characer_dropdown == "Loot bag":
        prompt = f"A loot bag from a medieval fantasy adventurer and his equipments. On the floor also a {weapon_equipment} a {head_equipment}, a {hand_equipment}, a {chest_equipment}, a {waist_equipment}, and a {foot_equipment}. Please sure to use only medieval items that were possble to be made in that period. Inside the bag also gold coins. Atmospheric light, cavern, dungeon context. Unreal Engine render style, photorealistic, realistic fantasy style."
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
    
    message = f"Image generated successfully! Call the banners! \n\n=====ADVENTURER GENERATED===== \nID: {id}\nNAME: {name}\nWEAPON: {weapon_equipment}\nHEAD: {head_equipment}\nHAND: {hand_equipment}\nCHEST: {chest_equipment}\nWAIST: {waist_equipment}\nBEAST: {beast_last_battle}"
    file_name_extension = f"ID: {id}\nNAME: {name}\nWEAPON: {weapon_equipment}\nHEAD: {head_equipment}\nHAND: {hand_equipment}\nCHEST: {chest_equipment}\nWAIST: {waist_equipment}\n LAST BATTLE BEAST: {beast_last_battle}"

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"{path}/{timestamp}_{seed}_{model_alias.replace(' ', '_').lower()}_{characer_dropdown.replace(' ', '_').lower()}_{file_name_extension.replace(' ', '_').lower()}.png"
    
    # output_filename = f"{path}/{timestamp}_{seed}_{model_alias.replace(' ', '_').lower()}_{prompt_alias.replace(' ', '_').lower()}_{characer_dropdown.replace(' ', '_').lower()}_{file_name_extension.replace(' ', '_').lower()}.png"

    try:
        image.save(output_filename)
    except Exception as e:
        return None, f"ERROR: Failed to save image. Details: {e}"
    print("-----DONE!-----")
    print("-----CALL THE BANNERS!-----")

    return output_filename, message