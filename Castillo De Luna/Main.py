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


def initialize_game_world():
    # populate initial room items
    roomDict[1].add_item_in_room(itemDict['CANDLESTICK'])
    roomDict[2].add_item_in_room(itemDict['SWORD'])
    roomDict[3].add_item_in_room(itemDict['BACKPACK'])
    roomDict[4].add_item_in_room(itemDict['NOTE1'])
    roomDict[4].add_item_in_room(itemDict['ELIXIR'])
    roomDict[5].add_item_in_room(itemDict['ELIXIR'])
    roomDict[6].add_item_in_room(itemDict['KEY'])
    roomDict[8].add_item_in_room(itemDict['NECKLACE OF DRAGON BEADS'])
    # room.id: 2 is the foyer (starting room)
    player.set_room(roomDict[2])

def fight():
    # critical dmg multipler with 5% chance 
    dmg_array = [player.get_damage(),player.get_damage()*2]
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
    if not curr_room.get_items_in_room():
        print("> There are no items to pick up.")
    while curr_room.get_items_in_room():
        print(f"> There are {len(curr_room.get_items_in_room())} item(s) to pick up.")
        print_items_on_floor(curr_room.get_items_in_room())
        selection = input("Select the item you want to pick: ")
        if selection.upper() == "BACK": get_action()
        if itemDict[selection.upper()] in curr_room.get_items_in_room():
            item = itemDict[selection.upper()]
            player.add_item(item)
            curr_room.remove_item_in_room(itemDict[selection.upper()])
            print(f"> {item.get_name().title()} picked up and added to your inventory.")
    get_action()


def use_action():
    consumable_items = {}
    for item in player.get_inv():
        if item.is_consumable():
            if item.get_name() not in consumable_items:
                consumable_items[item.get_name()] = 1
            else:
                consumable_items[item.get_name()] += 1
        else:
            continue

    if len(consumable_items) < 1:
        print("> You have no items to use.")
        get_action()

    print("\n ================[USE]=============== ")
    for item, count in consumable_items.items():
        print(f"  > {count} x {item}")
    print(f" ====================================")
    print(f"[ HP:{player.get_health()}/{MAX_HEALTH} ]\n")
    selection = input("Select item to use: ").upper()
    if selection == "BACK": get_action()
    if selection in consumable_items.keys():
        print(f"> {itemDict[selection].firstMessage}")
        use_item(selection)
        player.drop_item(selection)
    else:
        print("Enter a valid item...")
        use_action()


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
            get_action() 
        # no adj room in inputted direction
        else:
            print("There is nothing in that direction... ")
            move() 
        
    except KeyError:
        print("That is not a valid direction.")
        move() 


def increase_health(item):
    player.set_health(player.get_health() + item.restoreHealth)
    print(f"> HP + {item.restoreHealth} --> HP: {player.get_health()}/{MAX_HEALTH}")


def equip_action():
    if len(player.get_equipped()) < 1:
        print("> You have no items equipped.")
        get_action()

    print("\n ============[EQUIPMENT]=========== ")
    for item in player.get_equipped():
        print(f"  > {item.get_name().upper()}")
    print(f" =================================== \n")

    selection = input("Select item to unequip: ").upper()
    if selection == "BACK": get_action()
    if itemDict[selection] in player.get_equipped():
        print(f"> {itemDict[selection].firstMessage}")
        unequip_weapon(itemDict[selection])
    else:
        print("Enter a valid item...")
        equip_action()



def equip_weapon(item):
    if item not in player.get_equipped():
        player.add_equip(item)
        print(f"> EQUIPPED: {item.get_name().title()} -- DMG: +{item.damage} --> DMG: {player.get_damage() + item.damage}")
        player.set_damage(player.get_damage() + item.damage)
        
    else:
        print(f"{item.get_name().title()} already equipped.")
    get_action()


def unequip_weapon(item):
    print(f"> UNEQUIPPED: {item.get_name().title()} -- DMG -{item.damage} --> DMG: {player.get_damage() - item.damage}")
    player.set_damage(player.get_damage() - item.damage)
    player.remove_equip(item)


def use_item(itemSelection): # to continue 
    item = itemDict[itemSelection]
    if item.is_consumable():
        # using elixir item, increases health by item spec if max health is not yet reached
        if item.restoreHealth:
            if player.get_health() >= MAX_HEALTH:
                print(f"> [ HP: {player.get_health()}/{MAX_HEALTH} ] -- MAX HP ALREADY REACHED")
                get_action() 
            else:
                increase_health(item)
            # removes consumable item from player inventory when used
            player.rem_inv(item)
    elif item.is_weapon():
        equip_weapon(item)


    
def drop_item(item):
    item = itemDict[item]
    while True:
        if item in player.get_equipped():
            action = input(f"{item.get_name().title()} is currently equipped. Dropping this item will unequip it. Do you want to drop {item.get_name().title()}? [Y/N]: ").upper()
            unequip_weapon(item)
        if item not in player.get_equipped() or action == "Y":
            player.drop_item(item)
            print(f"Dropping {item.get_name().title()} from inventory...")
            curr_room = player.get_room()
            curr_room.add_item_in_room(item)
        open_inventory()


def get_inventory_capacity():
    if itemDict['BACKPACK'] in player.get_equipped():
        return 10
    else:
        return DEFAULT_INVENTORY_SIZE


def print_inventory(inv):
    print("\n ============[ INVENTORY ]============ ")
    for item, count in inv.items():
        print(f"  > {count} x {item}")
    print(f" ===============[ {(len(player.get_inv()))}/{get_inventory_capacity()} ]=============== \n")



def open_inventory():
    # populate inventory items 
    inv = {}
    for item in player.get_inv():
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
    print(f"> {player.get_name()} [ HP: {player.get_health()}/{MAX_HEALTH} ---- DMG: {player.get_damage()} ]")



def get_action():
    while True:
        ParseVerbs.list_available_verbs()
        action = input(f"[{player.get_room().get_room_name().upper()}]: ").upper()
        ParseVerbs.check_verb(action)
        # action to move player in world 
        if action == "GO":
            move()
        elif action == "PICKUP":
            pick_up_items(player.get_room())
        elif action == "INV":
            open_inventory()
        elif action == "USE":
            use_action()
        elif action == "EQUIP":
            equip_action()
        elif action == "STATS":
            check_stats()
        elif action == "QUIT":
            quit()



if __name__ == "__main__":
    GameStart.start_of_game()
    initialize_game_world()
    name = input("Let's start with your name: ").title()
    player.set_name("Noble " + name)
    time.sleep(0.5)
    print("Hello " + player.get_name() + ".")
    print("GAME STORYLINE START --------------------------------")
    time.sleep(0.5)
    print("enter BACK at any prompt to go back to the previous menu.")

    get_action() 
        

    GameEnd.end_of_game()
