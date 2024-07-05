# Task 1: Setting Up a Python Virtual Environment and Installing Packages

# Task 2: Fetching Data from the Pokémon API

import requests
import json

response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')

# Check the status of our request respobnse (using the status_code attribute)
print(response.status_code)

pokemon = response.json()
abilities = [ability['ability']['name'] for ability in pokemon['abilities']]

print(pokemon["name"].title()) # Pokemon name
print(abilities)


# Task 3: Analyzing and Displaying Data
def fetch_pokemon_data(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data for {pokemon_name}. Status code: {response.status_code}")
        return None
    

def calculate_average_weight(pokemon_list):
    total_weight = sum(pokemon['weight'] for pokemon in pokemon_list)
    return total_weight / len(pokemon_list)

pokemon_names = ["pikachu", "arbok", "spearow"]
pokemon_data = []

for name in pokemon_names:
    data = fetch_pokemon_data(name)
    if data:
        pokemon_data.append(data)

if pokemon_data:
    for pokemon in pokemon_data:
        name = pokemon['name']
        abilities = [ability['ability']['name'] for ability in pokemon['abilities']]
        print(f"Name: {name.title()}")
        print("Abilities:")
        for ability in abilities:
            print(f"- {ability.title()}")
        print()

    average_weight = calculate_average_weight(pokemon_data)
    print(f"Average Weight: {average_weight} hectograms")