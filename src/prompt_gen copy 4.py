from metadata.metadata import fetch_metadata

def prompt_gen(adventurer_id, scene_dropdown):
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
    gold_equipment = adventurer['gold']
    beast_last_battle = adventurer['beast']

    # Check for weapon = None to fix eventual generator mistakes
    if weapon_equipment == None:
        weapon_sentence = "holding nothing in his hands"
    else:   
        weapon_sentence = f"holding only a {weapon_equipment}"
    
    # if character_dropdown == "Wizard":
    #     character_attack_sentence = f"The adventurer is attacking using powerful magic"
    # else:
    #     character_attack_sentence = f"The adventurer is attacking using his {weapon_equipment}"


    # Set the custom prompt variables
    if scene_dropdown == "Adventurer Portait":
        prompt = f"A portait of a medieval, fantasy adventurer, {weapon_sentence}. He is also equiped in the head with a {head_equipment}, the hands with {hand_equipment}, the chest with a {chest_equipment}, and the waist with a {waist_equipment}. All equipments are strictly medieval, crafted from materials and techniques possible in that era. Make the adventurer unshaved and dirty, he have been figthing for days down into the dungeons. Torchlit light dungeon environment. Unreal Engine render style, photorealistic, atmospheric dark light, realistic fantasy style."

    if scene_dropdown == "Beast Portait":
        prompt = f"A massive {beast_last_battle} stands deep within the confines of a dark, foreboding dungeon. Its eyes glow faintly in the dark. It roars menacingly surrounded by broken weapons and bones of his past preys. Torchlit environment, underground dungeon. Unreal Engine render style, photorealistic, atmospheric dark lights, realistic fantasy style."
    
    if scene_dropdown == "Last Battle":
        prompt = f"A battle between a medieval fantasy adventurer and a massive {beast_last_battle} deep within the confines of a dark, foreboding dungeon. The adventurer is {weapon_sentence}. He is equipped with {head_equipment} on his head, {hand_equipment} on his hands, {chest_equipment} on his chest, {waist_equipment} around his waist, and {foot_equipment} on his feet. All equipment is strictly medieval, crafted from materials and techniques possible in that era. The {beast_last_battle} stands in a dark undergroud dungeon. Its eyes glow faintly in the dark. It roars menacingly, surrounded by broken weapons, scattered bones, and the remnants of past adventurers who failed to defeat it. The adventurer attacks using his {weapon_equipment} or powerful magic, the glow of his spells or the glint of his weapon illuminating the damp, moss-covered stone walls. The air is thick with the scent of mildew and blood, and the sound of dripping water echoes in the distance. Unreal Engine render style, photorealistic, realistic fantasy style."

    elif scene_dropdown == "Loot Bag":
        prompt = f"A loot bag from a medieval fantasy adventurer and his equipments. On the floor also a {weapon_equipment} a {head_equipment}, a {hand_equipment}, a {chest_equipment}, a {waist_equipment}, and a {foot_equipment}. All equipment is strictly medieval, crafted from materials and techniques possible in that era. Inside the bag {gold_equipment} gold coins. Atmospheric light, underground dungeon context. Torchlit environment. Unreal Engine render style, photorealistic, realistic fantasy style."
    else:       
        pass

    return adventurer, prompt

