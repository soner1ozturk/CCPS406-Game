import json
from Character import *
from Rooms import *
from Items import *
assets="assetText.json"

characterList = []
roomsList = []
itemsList = []
gameData=[]
messagesList=[]

# load assets from json file and populates objects 
with open(assets, 'r') as json_file:
    assetData = json.loads(json_file.read())
    #for words in assetData['gameData']:
    #    gameData.append(words)
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
    #for words in assetData['messages']:
    #    messagesList.append(words)

# characters 
player = characterList[0]
evandor = characterList[1]

#rooms for accessing, room id is key 
roomDict = {}
for room in roomsList:
    roomDict[room.id] = room 

#items for accessing, item name.upper() is key 
itemDict = {}
for item in itemsList:
    itemDict[item.getName()] = item


player.addInv(itemDict['SWORD'])

