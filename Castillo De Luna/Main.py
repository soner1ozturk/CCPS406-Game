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
    try:
        if player.getAdjRooms()[direction]:
            # updates player location and reprompts for next action
            newRoom = roomDict[player.getAdjRooms()[direction]]
            player.setRoom(newRoom)
            print(f">  Entering the {newRoom.getRoomName()}... ")
            get_action() 
        # no adj room in inputted direction
        else:
            print("There is nothing in that direction... ")
            move() 
    except KeyError:
        print("That is not a valid direction.")
        move() 

def increase_health(item):
    player.setHealth(item.restoreHealth)
    print(f" > HP + {item.restoreHealth} ---> HP: {player.getHealth()}/{MAX_HEALTH}")


def equip_weapon(item):
    if item not in player.getEquipped():
        player.addEquip(item)
        print(player.equipped)
        print (item in player.equipped)
        player.setDamage(item.damage)
        print(f"{item.getName()} equipped ---> DMG: {player.getDamage()}/{MAX_HEALTH}")
        
    else:
        print("Item already equipped.")
    get_action()



def use_item(itemSelection): # to continue 
    item = itemDict[itemSelection]
    if item.isConsumable():
        # using elixir item, increases health by item spec if max health is not yet reached
        if item.restoreHealth:
            if player.getHealth() >= MAX_HEALTH:
                print(f"HP: {player.getHealth()}/{MAX_HEALTH} -- MAX HP ALREADY REACHED")
                get_action() 
            else:
                increase_health(item)
        # removes consumable item from player inventory when used
        player.remInv(item)

    elif item.isWeapon():
        equip_weapon(item)
        pass


def open_inventory():
    # populate inventory items 
    inv = {}
    for item in player.getInv():
        if item.getName() not in inv:
            inv[item.getName()] = 1
        else:
            inv[item.getName()] += 1
    if len(inv) == 0:
        print("Inventory is empty... ")
    # display inventory and prompts for selection 
    else:
        print(inv)
        while True:
            selection = input("Opening inventory, select item:  ").upper() 
            if selection in inv.keys():
                # print("Using " + selection) # TODO: implement item use functionality
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
    player.setRoom(roomDict[2])
    time.sleep(1)
    print("Hello " + player.getName() + ".")
    print("GAME STORYLINE START --------------------------------")
    time.sleep(1)

    get_action() 
        


    GameEnd.end_of_game()