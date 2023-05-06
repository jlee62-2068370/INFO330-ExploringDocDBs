from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemon']
pokemonColl = pokemonDB['pokemon_data']
print("I found " + str(pokemonColl.count_documents({})) + " pokemon")
