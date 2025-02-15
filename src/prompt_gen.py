from metadata.metadata import fetch_metadata

def prompt_gen(adventurer_id, scene_dropdown):
    adventurer = fetch_metadata(adventurer_id)
    print(f"\nNAME: {adventurer['name']}")

    id = adventurer['id']
    name = adventurer['name']
    weapon_equipment = adventurer['weapon']
    head_equipment = adventurer['head']
    hand_equipment = adventurer['hand']
    chest_equipment = adventurer['chest']
    waist_equipment = adventurer['waist']
    foot_equipment = adventurer['foot']
    gold_equipment = adventurer['gold']
    adventurer_health = adventurer['health']
    beast_last_battle = adventurer['beast']
    beast_health = adventurer['beastHealth']

    # Check for weapon = None to fix eventual generator mistakes
    if weapon_equipment == None:
        weapon_equipment = "barehands"
    else:   
        weapon_sentence = f"holding only a {weapon_equipment}"
    
    # if character_dropdown == "Wizard":
    #     character_attack_sentence = f"The adventurer is attacking using powerful magic"
    # else:
    #     character_attack_sentence = f"The adventurer is attacking using his {weapon_equipment}"

    # Function to build equipment sentence dynamically
    def build_equipment_sentence(**equipment):
        sentences = []
        
        # Weapon
        if equipment.get("weapon_equipment"):
            sentences.append(f"holding a {equipment['weapon_equipment']}")
        else:
            sentences.append("holding nothing in his hands (bare hands)")
        
        # Head
        if equipment.get("head_equipment"):
            sentences.append(f"wearing a {equipment['head_equipment']} on his head")
        else:
            sentences.append("with no head protection (bare head)")
        
        # Hands
        if equipment.get("hand_equipment"):
            sentences.append(f"wearing {equipment['hand_equipment']} on his hands")
        else:
            sentences.append("with no hand protection (bare hands)")
        
        # Chest
        if equipment.get("chest_equipment"):
            sentences.append(f"wearing a {equipment['chest_equipment']} on his chest")
        else:
            sentences.append("with no chest armor (bare chest)")
        
        # Waist
        if equipment.get("waist_equipment"):
            sentences.append(f"wearing a {equipment['waist_equipment']} around his waist")
        else:
            sentences.append("with no waist equipment (bare waist)")
        
        # Feet
        if equipment.get("foot_equipment"):
            sentences.append(f"wearing {equipment['foot_equipment']} on his feet")
        else:
            sentences.append("with no foot protection (bare feet)")
        
        return ", ".join(sentences)

    # Example usage
    equipment_sentence = build_equipment_sentence(
        weapon_equipment=weapon_equipment,
        head_equipment=head_equipment,
        hand_equipment=hand_equipment,
        chest_equipment=chest_equipment,
        waist_equipment=waist_equipment,
        foot_equipment=foot_equipment
    )

    # Set the custom prompt variables
    if scene_dropdown == "Adventurer Portait":
        prompt = f"A portrait of a medieval, fantasy adventurer, {equipment_sentence}. All equipment is strictly medieval, crafted from materials and techniques possible in that era. Make the adventurer unshaved and dirty, as if he has been fighting for days down in the dungeons. Torchlit light environment. Foreboding dungeon scene. Unreal Engine render style, photorealistic, atmospheric dark light, realistic fantasy style."
        
    elif scene_dropdown == "Beast Portait":
        prompt = f"A portait of a massive {beast_last_battle} in a dark, foreboding dungeon. Its eyes glow faintly in the dark. It roars menacingly surrounded by broken weapons and bones of his past preys. Torchlit environment, underground dungeon. Unreal Engine render style, photorealistic, atmospheric dark lights, realistic fantasy style."

    elif scene_dropdown == "Encounter":
        prompt = f"A close-up shot of the {beast_last_battle}'s piercing eye, glowing faintly in the dim light of a torchlit dungeon. Intricate details of the beast's scaly or furred skin surround the eye, with faint scars and ancient markings hinting at its long history of battles. Torchlit environment. The atmosphere is tense, with shadows dancing across the dungeon walls and the faint glint of broken weapons and bones scattered nearby. Unreal Engine render style, photorealistic, atmospheric dark lighting, hyper-detailed, realistic fantasy style."
    
    elif scene_dropdown == "Last Battle":
        prompt = f"A battle between a medieval fantasy adventurer and a massive {beast_last_battle} deep within the confines of a dark, foreboding dungeon. The adventurer is {equipment_sentence}. All equipment is strictly medieval, crafted from materials and techniques possible in that era. The {beast_last_battle} stands in a dark undergroud dungeon. Its eyes glow faintly in the dark. It roars menacingly, surrounded by broken weapons and bones of his past preys. The adventurer is attacking using his {weapon_equipment} and powerful magic, the glow of his spells or the glint of his weapon illuminate the stone walls. The dungeon is dimly lit by flickering torches, their light casting long, ominous shadows across the ancient, cracked floor. Unreal Engine render style, photorealistic, realistic fantasy style."

    elif scene_dropdown == "Final Scene":
        print("===FINAL SCENE===")
        print(f"adv health: {adventurer_health}")
        if adventurer_health != 0:
            print("\n=====THE ADVENTURER IS STILL ALIVE2=====")
            prompt = f"A climactic battle between a medieval fantasy adventurer and a massive {beast_last_battle} deep within the confines of a dark, foreboding dungeon. The adventurer has emerged victorious, standing tall over the slain {beast_last_battle}. The beast lies defeated, its massive form crumpled on the dungeon floor, its faintly glowing eyes dimming as life fades. The adventurer is {equipment_sentence}, their equipment battered but intact, a testament to their skill and resilience. All equipment is strictly medieval, crafted from materials and techniques possible in that era. The scene takes place in a dark underground dungeon, dimly lit by flickering torches. The adventurer's breath is visible in the cold air, their expression a mix of exhaustion and triumph. The dungeon walls are damp and covered in moss, with ancient runes carved into the stone. Unreal Engine render style, photorealistic, realistic fantasy style, highly detailed, cinematic lighting, and atmospheric effects."
        else:       
            print("\n=====THE ADVENTURER IS DEAD2=====")
            prompt = f"Close-up shot of a dramatic battle between a medieval fantasy adventurer and a massive {beast_last_battle} deep within the confines of a dark, foreboding dungeon. The {beast_last_battle} has emerged victorious, standing triumphantly over the fallen adventurer. The adventurer lies defeated, {equipment_sentence}. All equipment is strictly medieval, crafted from materials and techniques possible in that era. The scene takes place in a dark underground dungeon, dimly lit by flickering torches. The {beast_last_battle}'s eyes glow faintly in the dark, casting an eerie light. The dungeon walls are damp and covered in moss, with ancient runes carved into the stone. Unreal Engine render style, photorealistic, realistic fantasy style, highly detailed, cinematic lighting, and atmospheric effects."
    else:       
        pass

    return adventurer, prompt

