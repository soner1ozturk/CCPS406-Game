from AssetBuilder import *
from Character import *
import GameStart
import GameEnd
import ParseVerbs
import time

def quit(): 
    print("Exiting game...")
    time.sleep(1)
    exit()

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

def increase_health(item):
    player.health = min(player._getHealth() + item.restoreHealth, MAX_HEALTH)
    print(f" > HP + {item.restoreHealth} ---> HP: {player._getHealth()}/{MAX_HEALTH}")
    

def use_item(itemSelection): # to continue 
    if itemDict[itemSelection].isConsumable():
        # using elixir item, increases health by item spec if max health is not yet reached
        if itemSelection == "ELIXIR":
            if player._getHealth() >= MAX_HEALTH:
                print(f"HP: {player._getHealth()}/{MAX_HEALTH} -- MAX HP ALREADY REACHED")
                # returns for reprompt 
                get_action() 
            # increases health as per item spec
            increase_health(itemDict[itemSelection])
        # removes consumable item from player inventory when used
        player._remInv(itemDict[itemSelection])

    elif itemDict[itemSelection].isWeapon():
        pass


def open_inventory():
    # populate inventory items 
    inv = {}
    for item in player._getInv():
        if item._getItemName().upper() not in inv:
            inv[item._getItemName().upper()] = 1
        else:
            inv[item._getItemName().upper()] += 1
    if len(inv) == 0:
        print("Inventory is empty... ")
    # display inventory and prompts for selection 
    else:
        while True:
            print(inv)
            selection = input("Opening inventory, select item:  ").upper() 
            if selection in inv.keys():
                print("Using " + selection) # TODO: implement item use functionality
                use_item(selection)
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
        elif action == "QUIT":
            quit()
        


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