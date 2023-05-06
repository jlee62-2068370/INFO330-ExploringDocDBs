import random
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

def fetch(pokemonid):
    return pokemonColl.find_one({"pokedex_number":pokemonid})

def battle(pokemon1, pokemon2):
    print("Let the Pokemon battle begin! ================")
    print("It's " + pokemon1['name'] + " vs " + pokemon2['name'])
    poke1 = 0
    poke2 = 0

    for stat in ['hp', 'attack', 'defense', 'speed', 'sp_attack', 'sp_defense']:
        if pokemon1[stat] > pokemon2[stat]:
            poke1 += 1
            print(pokemon1['name'] + " has the advantage in " + stat +
                  ". One point for " + pokemon1['name'] + "!")
        elif pokemon2[stat] > pokemon1[stat]:
            poke2 += 1
            print(pokemon2['name'] + "'s " + stat + " is superior. One point for "
                  + pokemon2['name'] + "!")

    print("The results are in!")
    if poke1 > poke2:
        print(pokemon1['name'] + " with " + str(poke1) + " points, wins the battle!")
    elif poke1 < poke2:
        print(pokemon2['name'] + " with " + str(poke2) + " points, wins the battle!")
    else:
        print(pokemon1['name'] + " and " + pokemon2['name'] + " tie in points, it's a draw!")

def main():
    # Fetch two pokemon from the MongoDB database
    pokemon1 = fetch(random.randrange(801))
    pokemon2 = fetch(random.randrange(801))

    # Pit them against one another
    battle(pokemon1, pokemon2)

main()
