from AssetBuilder import *
import Character
import GameStart
import GameEnd
import ParseVerbs
import time

def move():
    direction = input('Which direction to move? [N/S/E/W]: ').upper()
    if player._getRoom().adjRooms[direction] != None:
        # updates player location and reprompts for next action
        newRoom = roomDict[player._getRoom().adjRooms[direction]]
        player._setRoom(newRoom)
        print(f">  Entering the {newRoom._getRoomName()}... ")
        get_action() 
    # no adj room in inputted direction
    else:
        print("There is nothing in that direction... ")
        move() 

def open_inventory():
    # populate inventory items 
    inv = {}
    for i in player._getInv():
        if i.upper() not in inv:
            inv[i.upper()] = 1
        else:
            inv[i.upper()] += 1
    if len(inv) == 0:
        print("Inventory is empty... ")
    else:
        while True:
            print(inv)
            selection = input("Opening inventory, select item:  ").upper() 
            if selection in inv.keys():
                print("Using " + selection) # TODO: implement item use functionality 
                break
            else:
                print("Enter a valid inventory item...")
                open_inventory()
    get_action()
         
        

def get_action():
    while True:
        ParseVerbs.list_available_verbs()
        action = input("What To Do: ").upper()
        ParseVerbs.check_verb(action)
        # action to move player in world 
        if action == "GO":
            move()
        elif action == "INV":
            open_inventory()
        

        get_action()
        break 


if __name__ == "__main__":
    GameStart.start_of_game()
    name = input("Let's start with your name: ")
    player.setName(name)
#   # room.id: 2 is the foyer (starting room)
    player._setRoom(roomDict[2])
    time.sleep(1)
    print("Hello " + player.getName() + ".")
    print("GAME STORYLINE START --------------------------------")
    time.sleep(1)

    get_action() 
        


    GameEnd.end_of_game()