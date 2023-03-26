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
    dmg_array = [player.get_Damage(),player.get_Damage()*2]
    dmg_array_weights = [0.95, 0.05]

    print(random.choices(dmg_array, k=1, weights = dmg_array_weights)[0])


def print_items_on_floor(items_list):
    items_on_floor = {}
    for item in items_list:
        if item.get_name() not in items_on_floor:
            items_on_floor[item.get_name()] = 1
        else:
            items_on_floor[item.get_name()] += 1

    print("\n ==================================== ")
    for item, count in items_on_floor.items():
        print(f"  > {count} x {item}")
    print(f" ==================================== \n")


def pick_up_items(curr_room):
    while curr_room.get_items_in_rooms(): 
        print_items_on_floor(curr_room.get_items_in_rooms())
        selection = input("Select the item you want to pick: ")
        if itemDict[selection.upper()] in curr_room.get_items_in_rooms():
            item = itemDict[selection.upper()]
            player.add_Item(item)
            curr_room.remove_Item_In_Room(itemDict[selection.upper()])
            print(f"> {item.get_name().title()} picked up and added to your inventory.")
    get_action()

def move():
  
    direction = input('Which direction to move? [ N ] [ S ] [ E ] [ W ]: ').upper()
    try:
        if direction == "BACK": get_action()
        if player.get_adj_rooms()[direction]:
            # updates player location and reprompts for next action
            newRoom = roomDict[player.get_adj_rooms()[direction]]
            player.set_room(newRoom)
            print(f">  Entering the {newRoom.get_room_name()}... ")
            newRoom.get_room_message()
            # if items on floor, prompt to ask to pick up items
            if newRoom.items_in_room: 
                selection = input(f"There are {len(newRoom.get_items_in_rooms())} item(s) on the floor, would you like to pick them up? [Y/N]: ").upper()
                if selection == "BACK" or selection == "N": get_action()
                if selection == "Y": pick_up_items(newRoom)
                else: 
                    print("Invalid selection...")
                    selection = input(f"There are {len(newRoom.get_items_in_rooms())} item(s) on the floor, would you like to pick them up? [Y/N]: ").upper()
                
            get_action() 
        # no adj room in inputted direction
        else:
            print("There is nothing in that direction... ")
            move() 
        
    except KeyError:
        print("That is not a valid direction.")
        move() 


def increase_health(item):
    player.set_Health(item.restoreHealth)
    print(f"> HP + {item.restoreHealth} --> HP: {player.get_Health()}/{MAX_HEALTH}")


def equip_weapon(item):
    if item not in player.get_Equipped():
        player.addEquip(item)
        print(f"> EQUIPPED: {item.get_name().title()} -- DMG: +{item.damage} --> DMG: {player.get_Damage() + item.damage}")
        player.set_Damage(item.damage)
        
    else:
        print(f"{item.get_name().title()} already equipped.")
    get_action()



def use_item(itemSelection): # to continue 
    item = itemDict[itemSelection]
    if item.is_Consumable():
        # using elixir item, increases health by item spec if max health is not yet reached
        if item.restoreHealth:
            if player.get_Health() >= MAX_HEALTH:
                print(f"> [ HP: {player.get_Health()}/{MAX_HEALTH} ] -- MAX HP ALREADY REACHED")
                get_action() 
            else:
                increase_health(item)
            # removes consumable item from player inventory when used
            player.rem_Inv(item)
    elif item.is_Weapon():
        equip_weapon(item)


    
def drop_item(item):
    item = itemDict[item]
    player.drop_Item(item)
    print(f"Dropping {item.get_name().title()} from inventory...")
    curr_room = player.get_Room()
    curr_room.add_Item_In_Room(item)
    print(curr_room.get_items_in_rooms())
    
    open_inventory()


def get_inventory_capacity():
    if itemDict['BACKPACK'] in player.get_Equipped():
        return 10
    else:
        return DEFAULT_INVENTORY_SIZE

def print_inventory(inv):
    print("\n ============[ INVENTORY ]============ ")
    for item, count in inv.items():
        print(f"  > {count} x {item}")
    print(f" ===============[ {(len(player.get_Inv()))}/{get_inventory_capacity()} ]=============== \n")

def open_inventory():
    # populate inventory items 
    inv = {}
    for item in player.getInv():
        if item.get_name() not in inv:
            inv[item.get_name()] = 1
        else:
            inv[item.get_name()] += 1
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
    print(f"> {player.get_name()} [ HP: {player.get_Health()}/{MAX_HEALTH} ---- DMG: {player.get_Damage()} ]")

def get_action():
    while True:
        ParseVerbs.list_available_verbs()
        action = input(f"[{player.get_Room().get_room_name().upper()}]: ").upper()
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
    player.set_Name("Noble " + name)
#   # room.id: 2 is the foyer (starting room)
    player.set_room(roomDict[2])
    time.sleep(0.5)
    print("Hello " + player.get_name() + ".")
    print("GAME STORYLINE START --------------------------------")
    time.sleep(0.5)
    print("enter BACK at any prompt to go back to the previous menu.")

    get_action() 
        


    GameEnd.end_of_game()