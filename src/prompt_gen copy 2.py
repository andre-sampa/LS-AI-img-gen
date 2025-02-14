from metadata.metadata import fetch_metadata

def prompt_gen(adventurer_id, character_dropdown, scene_dropdown):
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
    
    if character_dropdown == "Wizard":
        character_attack_sentence = f"The adventurer is attacking using powerful magic"
    else:
        character_attack_sentence = f"The adventurer is attacking using his {weapon_equipment}"


    # Set the custom prompt variables
    if scene_dropdown == "Adventurer Portait":
        prompt = f"A portait of a medieval, fantasy adventurer, {weapon_sentence}. Make the adventurer dressed as a {character_dropdown}. He is also equiped in the head with a {head_equipment}, the hands with {hand_equipment}, the chest with a {chest_equipment}, and the waist with a {waist_equipment}. Please be sure to use only medieval items that were possble to be made in that period. Make the adventurer unshaved and dirty, he have been figthing for days down into the dungeons. Unreal Engine render style, photorealistic, atmospheric light, realistic fantasy style."

    if scene_dropdown == "Beast Portait":
        prompt = f"A massive {beast_last_battle} stands in its natural domain—a place that reflects its primal essence. The beast's eyes burn with an eerie, intelligent light, and its powerful limbs are poised for action, as if ready to pounce or defend its territory. It roars menacingly, surrounded by broken weapons and bones. In the background, a dramatic landscape unfolds: dense forests, underground dungeons, jagged mountains, dark caves, or misty swamps. The atmosphere is both terrifying and awe-inspiring, capturing the essence of a fantasy world where magic and monsters reign supreme. Unreal Engine render style, photorealistic, atmospheric light, realistic fantasy style."
    
    if scene_dropdown == "Last Battle":
        prompt = f"A battle between a medieval fantasy adventurer, and a massive {beast_last_battle}. The adventurer is {weapon_sentence}. He is also equiped in the head with {head_equipment}, the hands with {hand_equipment}, the chest with {chest_equipment}, the waist with {waist_equipment}, the feet with {foot_equipment}. Use only medieval items that were possible to be made in that period. The {beast_last_battle} stands in its natural domain—a place that reflects its primal essence. The beast's eyes burn with an eerie, intelligent light, and its powerful limbs are poised for action, as if ready to pounce or defend its territory. It roars menacingly, surrounded by broken weapons and bones. {character_attack_sentence}. In the background, a dramatic landscape unfolds: dense forests, underground dungeons, jagged mountains, dark caves, or misty swamps. The atmosphere is both terrifying and awe-inspiring, capturing the essence of a fantasy world where magic and monsters reign supreme. Unreal Engine render style, photorealistic, realistic fantasy style."

    elif scene_dropdown == "Loot Bag":
        prompt = f"A loot bag from a medieval fantasy adventurer and his equipments. On the floor also a {weapon_equipment} a {head_equipment}, a {hand_equipment}, a {chest_equipment}, a {waist_equipment}, and a {foot_equipment}. Please sure to use only medieval items that were possble to be made in that period. Inside the bag {gold_equipment} gold coins. Atmospheric light, cavern, dungeon context. Unreal Engine render style, photorealistic, realistic fantasy style."
    else:       
        pass

    return adventurer, prompt

