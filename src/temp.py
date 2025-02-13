Dungeon context, stones, fire and low light.





 if characer_dropdown == "Portait":
        prompt = f"A portait of a medieval, fantasy adventurer, holding a {weapon_equipment} (depending on his weapon, make the characer dressed as a warrior, or as a hunter or as a wizard). He is also equiped in the head with a {head_equipment}, the hands with {hand_equipment}, the chest with a {chest_equipment}, and the waist with a {waist_equipment}. Please be sure to use only medieval items that were possble to be made in that period. Make the adventurer unshaved and dirty, he have been figthing for days down into the dungeons. Unreal Engine render style, photorealistic, atmospheric light, realistic fantasy style."
    
    if characer_dropdown == "Last battle":
        prompt = f"A battle between a medieval fantasy adventurer, and a massive {beast_last_battle} monster. The adventurer is combating with a weapon: a {weapon_equipment} (depending on his equipment, make the characer dressed as a warrior, or as a hunter or as a wizard). He is also equiped in the head with {head_equipment}, the hands with {hand_equipment}, the chest with {chest_equipment}, the waist with {waist_equipment}, the fet with {foot_equipment}. Please sure to use only medieval items that were possble to be made in that period. Add details for the monster as well. The scene location is the natural ambient of the {beast_last_battle}. Unreal Engine render style, photorealistic, dark atmospheric light, realistic fantasy style."

    elif characer_dropdown == "Loot bag":
        prompt = f"A loot bag from a medieval fantasy adventurer and his equipments. On the floor also a {weapon_equipment} a {head_equipment}, a {hand_equipment}, a {chest_equipment}, a {waist_equipment}, and a {foot_equipment}. Please sure to use only medieval items that were possble to be made in that period. Inside the bag also gold coins. Atmospheric light, cavern, dungeon context. Unreal Engine render style, photorealistic, realistic fantasy style."
    else:       
        pass