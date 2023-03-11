import json
from Character import *
from Rooms import *
from Items import *
assets="assetText.json"

characterList = []
roomsList = []
itemsList = []


# load assets from json file and populates objects 
with open(assets, 'r') as json_file:
    assetData = json.loads(json_file.read())
    for character in assetData['character']['goodCharacter']:
        characterList.append(GoodCharacter(**character))
    for character in assetData['character']['badCharacter']:
        characterList.append(BadCharacter(**character))
    for room in assetData['room']: 
        roomsList.append(Room(**room))
    for item in assetData['items']['consumables']:
        itemsList.append(Consumable(**item))
    for item in assetData['items']['weapons']:
        itemsList.append(Weapon(**item))    

