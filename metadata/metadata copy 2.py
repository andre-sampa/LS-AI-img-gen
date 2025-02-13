import requests
import json  # Import the json module for saving data

# Define the GraphQL endpoint
url = "https://ls-indexer-sepolia.provable.games/graphql"

# Define the GraphQL queries
query = """
query MyQuery {
  adventurers(limit: 10, where: {id: {eq: 555}}) {
    owner
    id
    name
    strength
    vitality
    dexterity
    intelligence
    wisdom
    charisma
    level
    xp
    health
    beastHealth
    head
    hand
    chest
    waist
    foot
    weapon
    gold
    neck
    ring
    luck
    battleActionCount
    customRenderer
    statUpgrades
  }
}
"""

query2 = """
query MyQuery {
  battles(where: {adventurerId: {eq: 555}}) {
    adventurerId
    adventurerHealth
    beast
    beastHealth
    beastLevel
    seed
    attacker
    fled
    damageDealt
    criticalHit
    damageTaken
    damageLocation
    xpEarnedAdventurer
    xpEarnedItems
    goldEarned
    discoveryTime
  }
}
"""

# Define the request payloads
payload = {
    "query": query
}
payload2 = {
    "query": query2
}

# Send the POST requests to the GraphQL API
response = requests.post(url, json=payload)
response2 = requests.post(url, json=payload2)

# Check if the requests were successful
if response.status_code == 200 and response2.status_code == 200:
    # Parse the JSON responses
    data = response.json()
    data2 = response2.json()
    print("Data fetched successfully.")

    # Save the data to files
    with open("adventurers_data.json", "w") as file:
        json.dump(data, file, indent=4)  # Save with pretty-printing (indent=4)
    with open("adventurers_data2.json", "w") as file:
        json.dump(data2, file, indent=4)  # Save with pretty-printing (indent=4)
    print("Data saved to 'adventurers_data.json' and 'adventurers_data2.json'.")

    # Extract the list of adventurers from both queries
    adventurers = data.get("data", {}).get("adventurers", [])
    battles = data2.get("data", {}).get("battles", [])

    # Create a dictionary to map adventurers by their ID for quick lookup
    adventurers_dict = {adv["id"]: adv for adv in adventurers}

    # Add fields from the second query to the corresponding adventurer
    for adv2 in battles:
        adventurer_id = adv2["adventurerId"]
        if adventurer_id in adventurers_dict:
            print("here")
            # Add new fields to the existing adventurer
            adventurers_dict[adventurer_id].update(adv2)
        else:
            print("else")

    # Print each adventurer's details dynamically
    for adventurer in adventurers_dict.values():
        # Create a dictionary to store field values
        adventurer_data = adventurer  # Use the updated dictionary

        print("\n=====Adventurer Details=====")
        for key, value in adventurer_data.items():
            print(f"{key.capitalize()}: {value}")

        if adventurer_data['health'] != 0:
            print("\n=====THE ADVENTURER IS STILL ALIVE=====")
        else:
            print("\n=====THE ADVENTURER IS DEAD=====")

        # Example: Access specific fields
        print(f"\nEquipment list of {adventurer_data['name']}:")
        print(f"\nAdventurer Head: {adventurer_data.get('head', 'None')}")
        print(f"Hand: {adventurer_data.get('hand', 'None')}")
        print(f"Chest: {adventurer_data.get('chest', 'None')}")
        print(f"Waist: {adventurer_data.get('waist', 'None')}")
        print(f"Foot: {adventurer_data.get('foot', 'None')}")
        print(f"Weapon: {adventurer_data.get('weapon', 'None')}")
        print(f"Last combat: {adventurer_data.get('beast', 'Unknown')}")
        print(f"Beast Level: {adventurer_data.get('beastLevel', 'Unknown')}")
        print(f"Attacker: {adventurer_data.get('attacker', 'Unknown')}")
        print(f"Fled: {adventurer_data.get('fled', 'Unknown')}")
        print(f"Damage Dealt: {adventurer_data.get('damageDealt', 'Unknown')}")
        print(f"Damage Taken: {adventurer_data.get('damageTaken', 'Unknown')}")
        print(f"Crticial Hit: {adventurer_data.get('criticalHit', 'Unknown')}")
        print(f"Damage Location: {adventurer_data.get('damageLocation', 'Unknown')}")
        print(f"Beast Health: {adventurer_data.get('beastHealth', 'Unknown')}")
        print(f"Adventure Health: {adventurer_data.get('adventurerHealth', 'Unknown')}")

else:
    # Print detailed error information
    print(f"Failed to fetch data. Status codes: {response.status_code}, {response2.status_code}")
    print("Response 1 Headers:", response.headers)
    print("Response 1 Body:", response.text)
    print("Response 2 Headers:", response2.headers)
    print("Response 2 Body:", response2.text)