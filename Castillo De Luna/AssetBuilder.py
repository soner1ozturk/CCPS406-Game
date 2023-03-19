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


# characters 
mainChar = characterList[0]
evandor = characterList[1]

#rooms 
courtyard = roomsList[0]
foyer = roomsList[1]
armory = roomsList[2]
kitchen = roomsList[3]
diningRoom = roomsList[4]
chapel = roomsList[5]
library = roomsList[6]
grandHall = roomsList[7]
cellar = roomsList[8]
dungeon = roomsList[9]



