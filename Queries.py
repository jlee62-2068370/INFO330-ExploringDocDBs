from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/")
pokemonDB = mongoClient['pokemon']
pokemonColl = pokemonDB['pokemon_data']

# Write a query that returns all the Pokemon named "Pikachu". (1pt)
pikachu = pokemonColl.find_one({"name" : "Pikachu"})
print(pikachu['name'])
print("-----------------------")

# Write a query that returns all the Pokemon with an attack greater than 150. (1pt)
greater_than = pokemonColl.find({"attack" : { "$gt": 150 }})
for pokemon in greater_than:
    print(pokemon['name'], pokemon['attack'])
print("-----------------------")

# Write a query that returns all the Pokemon with an ability of "Overgrow" (1pt)
ability_overgrow = pokemonColl.find({ "abilities" : { "$regex" : "Overgrow" }})
for pokemon in ability_overgrow:
    print(pokemon['name'], pokemon['abilities'])