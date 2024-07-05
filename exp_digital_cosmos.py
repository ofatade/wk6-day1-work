import requests

# Task 1: Set up a Python Virtual Environment and Install Required Packages
# - Done in previous module

# Task 2: Fetch Data from a Space API

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    #process each planet info
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass = planet['mass']['massValue']
            orbit_period = planet['sideralOrbit']
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

# Task 3: Data Presentation and Analysis
def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    
    if response.status_code == 200:
        planets = response.json()['bodies']
        planet_data = []
        
        for planet in planets:
            if planet['isPlanet']:
                name = planet['englishName']
                mass = planet['mass']['massValue']
                orbit_period = planet['sideralOrbit']
                planet_data.append({
                    'name': name,
                    'mass': mass,
                    'orbit_period': orbit_period
                })
                print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

        return planet_data
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return []  
    

def find_heaviest_planet(planet_data):
    if not planet_data:
        return None
    return max(planet_data, key=lambda x: x['mass'])

planet_data = fetch_planet_data()

if planet_data:
    heaviest_planet = find_heaviest_planet(planet_data)

    if heaviest_planet:
        print(f"\nHeaviest planet: {heaviest_planet['name']}")
        print(f"Mass: {heaviest_planet['mass']}")

