import requests
import json  # Import the json module for saving data

# Define the GraphQL endpoint
url = "https://ls-indexer-sepolia.provable.games/graphql"

# Define the GraphQL query
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

# Define the request payload
payload = {
    "query": query
}

# Send the POST request to the GraphQL API
response = requests.post(url, json=payload)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    print("Data fetched successfully:")
    print(data)
    # Save the data to a file
    with open("adventurers_data.json", "w") as file:
        json.dump(data, file, indent=4)  # Save with pretty-printing (indent=4)
    print("Data saved to 'adventurers_data.json'.")

    # Extract the list of adventurers
    adventurers = data.get("data", {}).get("adventurers", [])

    # Print each adventurer's details dynamically
    for adventurer in adventurers:
        # Assign the 'hand' and 'head' fields to variables
        
        head = adventurer.get("head")
        hand = adventurer.get("hand")

        # Print the variables (for debugging)
        print(f"Hand: {hand_var}")
        print(f"Head: {head_var}")

        # Check if 'hand_var' is not None and call action()
        if hand_var is not None:
            print(hand_var)

        print("\n=====Adventurer Details=====")
        for key, value in adventurer.items():
            print(f"{key.capitalize()}: {value}")
            adventurer_data[key] = value  # Assign to dictionary

        if heatlh is not 0:
            print("\n=====THE ADVENTURER IS STILL ALIVE=====")
        else:
            print("\n=====THE ADVENTURER IS DEAD=====")
        # Example: Access specific fields
        print(f"\nEquipment list of {adventurer_data['name']}:")
        print(f"\nAdventurer Head: {adventurer_data['head']}")
        print(f"Hand: {adventurer_data['hand']}")
        print(f"Chest: {adventurer_data['chest']}")
        print(f"Waist: {adventurer_data['waist']}")
        print(f"Foot: {adventurer_data['foot']}")
        print(f"Weapon: {adventurer_data['weapon']}")
        print(f"Last combat: {adventurer_data['weapon']}")


else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
    print(response.text)