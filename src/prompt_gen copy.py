from metadata.metadata import fetch_metadata

def prompt_gen(adventurer_id, characer_dropdown):
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

    # Set the custom prompt variables
    if characer_dropdown == "Adventurer Portait":
        prompt = f"A portait of a medieval, fantasy adventurer, holding only a {weapon_equipment} (depending on his weapon, make the characer dressed as a warrior, or as a hunter or as a wizard). He is also equiped in the head with a {head_equipment}, the hands with {hand_equipment}, the chest with a {chest_equipment}, and the waist with a {waist_equipment}. Please be sure to use only medieval items that were possble to be made in that period. Make the adventurer unshaved and dirty, he have been figthing for days down into the dungeons. Unreal Engine render style, photorealistic, atmospheric light, realistic fantasy style."

    if characer_dropdown == "Beast Portait":
        prompt = f"A massive {beast_last_battle} stands in its natural domain—a place that reflects its primal essence. The beast's eyes burn with an eerie, intelligent light, and its powerful limbs are poised for action, as if ready to pounce or defend its territory. The air is thick with tension, and the ground is littered with signs of its dominance—broken terrain, scattered bones, or remnants of its prey. In the background, a dramatic landscape unfolds: dense forests, jagged mountains, dark caves, or misty swamps. The atmosphere is both terrifying and awe-inspiring, capturing the essence of a fantasy world where magic and monsters reign supreme. Unreal Engine render style, photorealistic, atmospheric light, realistic fantasy style."
    
    if characer_dropdown == "Last Battle":
        prompt = f"A battle between a medieval fantasy adventurer, and a massive {beast_last_battle}. The adventurer is holding only a {weapon_equipment}. He is also equiped in the head with {head_equipment}, the hands with {hand_equipment}, the chest with {chest_equipment}, the waist with {waist_equipment}, the feet with {foot_equipment}. Use only medieval items that were possible to be made in that period. The {beast_last_battle} stands in its natural domain—a place that reflects its primal essence. The beast's eyes burn with an eerie, intelligent light, and its powerful limbs are poised for action, as if ready to pounce or defend its territory. The the ground is littered with signs of its dominance—broken terrain, scattered bones, or remnants of its prey. The adventurer attacks using his {weapon_equipment} or powerful magic. In the background, a dramatic landscape unfolds: dense forests, jagged mountains, dark caves, or misty swamps. The atmosphere is both terrifying and awe-inspiring, capturing the essence of a fantasy world where magic and monsters reign supreme. Unreal Engine render style, photorealistic, realistic fantasy style."

    elif characer_dropdown == "Loot Bag":
        prompt = f"A loot bag from a medieval fantasy adventurer and his equipments. On the floor also a {weapon_equipment} a {head_equipment}, a {hand_equipment}, a {chest_equipment}, a {waist_equipment}, and a {foot_equipment}. Please sure to use only medieval items that were possble to be made in that period. Inside the bag also {gold_equipment} gold coins. Atmospheric light, cavern, dungeon context. Unreal Engine render style, photorealistic, realistic fantasy style."
    else:       
        pass

    return adventurer, prompt

