from AssetBuilder import *
from Character import *
import GameStart
import GameEnd
import ParseVerbs
import time
import random



def quit(): 
    print("Exiting game...")
    time.sleep(0.5)
    exit()

def fight(): 
    # critical dmg multipler with 5% chance 
    dmg_array = [player.getDamage(),player.getDamage()*2]
    dmg_array_weights = [0.95, 0.05]

    print(random.choices(dmg_array, k=1, weights = dmg_array_weights)[0])


def print_items_on_floor(items_list):
    items_on_floor = {}
    for item in items_list:
        if item.getName() not in items_on_floor:
            items_on_floor[item.getName()] = 1
        else:
            items_on_floor[item.getName()] += 1

    print("\n ==================================== ")
    for item, count in items_on_floor.items():
        print(f"  > {count} x {item}")
    print(f" ==================================== \n")


def pick_up_items(curr_room):
    while curr_room.getItemsInRoom(): 
        print_items_on_floor(curr_room.getItemsInRoom())
        selection = input("Select the item you want to pick: ")
        if itemDict[selection.upper()] in curr_room.getItemsInRoom():
            item = itemDict[selection.upper()]
            player.addItem(item)
            curr_room.removeItemInRoom(itemDict[selection.upper()])
            print(f"> {item.getName().title()} picked up and added to your inventory.")
    get_action()

def move():
  
    direction = input('Which direction to move? [ N ] [ S ] [ E ] [ W ]: ').upper()
    try:
        if direction == "BACK": get_action()
        if player.getAdjRooms()[direction]:
            # updates player location and reprompts for next action
            newRoom = roomDict[player.getAdjRooms()[direction]]
            player.setRoom(newRoom)
            print(f">  Entering the {newRoom.getRoomName()}... ")
            # update room visited flag
            if not newRoom.visited: newRoom.visited = True 
            # if items on floor, prompt to ask to pick up items 
            if newRoom.itemsInRoom: 
                selection = input(f"There are {len(newRoom.getItemsInRoom())} item(s) on the floor, would you like to pick them up? [Y/N]: ").upper()
                if selection == "BACK" or selection == "N": get_action()
                if selection == "Y": pick_up_items(newRoom)
                else: 
                    print("Invalid selection...")
                    selection = input(f"There are {len(newRoom.getItemsInRoom())} item(s) on the floor, would you like to pick them up? [Y/N]: ").upper()
                
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
    print(f"> HP + {item.restoreHealth} --> HP: {player.getHealth()}/{MAX_HEALTH}")


def equip_weapon(item):
    if item not in player.getEquipped():
        player.addEquip(item)
        print(f"> EQUIPPED: {item.getName().title()} -- DMG: +{item.damage} --> DMG: {player.getDamage() + item.damage}")
        player.setDamage(item.damage)
        
    else:
        print(f"{item.getName().title()} already equipped.")
    get_action()



def use_item(itemSelection): # to continue 
    item = itemDict[itemSelection]
    if item.isConsumable():
        # using elixir item, increases health by item spec if max health is not yet reached
        if item.restoreHealth:
            if player.getHealth() >= MAX_HEALTH:
                print(f"> [ HP: {player.getHealth()}/{MAX_HEALTH} ] -- MAX HP ALREADY REACHED")
                get_action() 
            else:
                increase_health(item)
            # removes consumable item from player inventory when used
            player.remInv(item)
    elif item.isWeapon():
        equip_weapon(item)


    
def drop_item(item):
    item = itemDict[item]
    player.dropItem(item)
    print(f"Dropping {item.getName().title()} from inventory...")
    curr_room = player.getRoom()
    curr_room.addItemInRoom(item)
    print(curr_room.getItemsInRoom())
    
    open_inventory()


def get_inventory_capacity():
    if itemDict['BACKPACK'] in player.getEquipped():
        return 10
    else:
        return DEFAULT_INVENTORY_SIZE

def print_inventory(inv):
    print("\n ============[ INVENTORY ]============ ")
    for item, count in inv.items():
        print(f"  > {count} x {item}")
    print(f" ===============[ {(len(player.getInv()))}/{get_inventory_capacity()} ]=============== \n")

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
        print_inventory(inv)
        while True:
            selection = input("Opening inventory, select item: ").upper()
            if selection == "BACK": get_action() 
            if selection in inv.keys():
                # print("Using " + selection) # TODO: implement item use functionality
                print(f"> {itemDict[selection].firstMessage}")
                use_or_drop = input(f"Do you want to use or drop {selection.title()}? [USE/DROP]: ").upper()
                if use_or_drop == "BACK": open_inventory()
                if use_or_drop == "USE":
                    use_item(selection)
                elif use_or_drop == "DROP":
                    drop_item(selection)
                else: 
                    print("Invalid selection...")
                    open_inventory()
            else:
                print("Enter a valid inventory item...")
                open_inventory()
    get_action()


def check_stats():
    print(f"> {player.getName()} [ HP: {player.getHealth()}/{MAX_HEALTH} ---- DMG: {player.getDamage()} ]")

def get_action():
    while True:
        ParseVerbs.list_available_verbs()
        action = input(f"[{player.getRoom().getRoomName().upper()}]: ").upper()
        ParseVerbs.check_verb(action)
        # action to move player in world 
        if action == "GO":
            move()
        elif action == "INV":
            open_inventory()
        elif action == "STATS":
            check_stats()
        elif action == "QUIT":
            quit()

        # get_action()
        # break 


if __name__ == "__main__":
    GameStart.start_of_game()
    name = input("Let's start with your name: ").title()
    player.setName("Noble " + name)
#   # room.id: 2 is the foyer (starting room)
    player.setRoom(roomDict[2])
    time.sleep(0.5)
    print("Hello " + player.getName() + ".")
    print("GAME STORYLINE START --------------------------------")
    time.sleep(0.5)
    print("enter BACK at any prompt to go back to the previous menu.")

    get_action() 
        


    GameEnd.end_of_game()