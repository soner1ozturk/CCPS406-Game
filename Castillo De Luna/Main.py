
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
    roomDict[1].add_Item_In_Room(itemDict['CANDLESTICK'])
    roomDict[2].add_Item_In_Room(itemDict['SWORD'])
    roomDict[3].add_Item_In_Room(itemDict['BACKPACK'])
    roomDict[4].add_Item_In_Room(itemDict['NOTE1'])
    roomDict[4].add_Item_In_Room(itemDict['ELIXIR'])
    roomDict[5].add_Item_In_Room(itemDict['ELIXIR'])
    roomDict[6].add_Item_In_Room(itemDict['KEY'])
    roomDict[8].add_Item_In_Room(itemDict['NECKLACE OF DRAGON BEADS'])
    # room.id: 2 is the foyer (starting room)
    player.set_Room(roomDict[2])

def fight(): 
    # critical dmg multipler with 5% chance 
    dmg_array = [player.get_Damage(),player.get_Damage()*2]
    dmg_array_weights = [0.95, 0.05]

    print(random.choices(dmg_array, k=1, weights = dmg_array_weights)[0])


def print_items_on_floor(items_list):
    items_on_floor = {}
    for item in items_list:
        if item.get_Name() not in items_on_floor:
            items_on_floor[item.get_Name()] = 1
        else:
            items_on_floor[item.get_Name()] += 1
    print("\n ==================================== ")
    for item, count in items_on_floor.items():
        print(f"  > {count} x {item}")
    print(f" ==================================== \n")


def pick_up_items(curr_room):
    if not curr_room.get_Items_In_Room(): 
        print("> There are no items to pick up.")
    while curr_room.get_Items_In_Room(): 
        print(f"> There are {len(curr_room.get_Items_In_Room())} item(s) to pick up.")
        print_items_on_floor(curr_room.get_Items_In_Room())
        selection = input("Select the item you want to pick: ")
        if selection.upper() == "BACK": get_action()
        if itemDict[selection.upper()] in curr_room.get_Items_In_Room():
            item = itemDict[selection.upper()]
            player.add_Item(item)
            curr_room.remove_Item_In_Room(itemDict[selection.upper()])
            print(f"> {item.get_Name().title()} picked up and added to your inventory.")
    get_action()


def use_action():
    consumable_items = {}

    for item in player.get_Inv():
        if item.is_Consumable():
            if item.get_Name() not in consumable_items:
                consumable_items[item.get_Name()] = 1
            else:
                consumable_items[item.get_Name()] += 1
        else:
            continue

    if len(consumable_items) < 1:
        print("> You have no items to use.")
        get_action() 
    
    print("\n ================[USE]=============== ")
    for item, count in consumable_items.items():
        print(f"  > {count} x {item}")
    print(f" =====================================")
    print(f"[ HP:{player.get_Health()}/{MAX_HEALTH} ]\n")
    selection = input("Select item to use: ").upper()
    if selection == "BACK": get_action() 
    if selection in consumable_items.keys():
        print(f"> {itemDict[selection].firstMessage}")
        use_item(selection)
        player.drop_Item(selection)
    else:
        print("Enter a valid item...")
        use_action()


def move():
    direction = input('Which direction to move? [ N ] [ S ] [ E ] [ W ]: ').upper()
    try:
        if direction == "BACK": get_action()
        if player.get_AdjRooms()[direction]:
            # updates player location and reprompts for next action
            newRoom = roomDict[player.get_AdjRooms()[direction]]
            player.set_Room(newRoom)
            print(f">  Entering the {newRoom.getRoomName()}... ")
            # update room visited flag
            if not newRoom.visited: newRoom.visited = True      
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


def equip_action():
    weapon_items = {}

    for item in player.get_Inv():
        if item.is_Weapon():
            if item.get_Name() not in weapon_items:
                weapon_items[item.get_Name()] = 1
            else:
                weapon_items[item.get_Name()] += 1
        else:
            continue

    if len(weapon_items) < 1:
        print("> You have no items to equip.")
        get_action() 

    print("\n ============[EQUIPMENT]=========== ")
    for item, count in weapon_items.items():
        print(f"  > {count} x {item}")
    print(f" =================================== \n")
    
    selection = input("Select item to use: ").upper()
    if selection == "BACK": get_action() 
    if selection in weapon_items.keys():
        print(f"> {itemDict[selection].firstMessage}")
        equip_weapon(itemDict[selection])
    else:
        print("Enter a valid item...")
        equip_action()



def equip_weapon(item):
    if item not in player.get_Equipped():
        player.add_Equip(item)
        print(f"> EQUIPPED: {item.get_Name().title()} -- DMG +{item.damage} --> DMG: {player.getDamage() + item.damage}")
        player.set_Damage(player.getDamage() + item.damage)
        
    else:
        print(f"{item.get_Name().title()} already equipped.")
    get_action()


def unequip_weapon(item):
    # player.add_Equip(item)
    print(f"> UNEQUIPPED: {item.get_Name().title()} -- DMG -{item.damage} --> DMG: {player.getDamage() - item.damage}")
    player.set_Damage(player.getDamage() - item.damage)
    player.removeEquip(item)


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
            player.drop_Item(item)
    elif item.is_Weapon():
        equip_weapon(item)

    
def drop_item(item):
    item = itemDict[item]
    while True:
        if item in player.get_Equipped():
            action = input(f"{item.get_Name().title()} is currently equipped. Dropping this item will unequip it. Do you want to drop {item.get_Name().title()}? [Y/N]: ").upper()
            unequip_weapon(item)
        if item not in player.get_Equipped() or action == "Y":
            player.drop_Item(item)
            print(f"Dropping {item.get_Name().title()} from inventory...")
            curr_room = player.get_Room()
            curr_room.add_Item_In_Room(item) 
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
    for item in player.get_Inv():
        if item.get_Name() not in inv:
            inv[item.get_Name()] = 1
        else:
            inv[item.get_Name()] += 1
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
    print(f"> {player.get_Name()} [ HP: {player.get_Health()}/{MAX_HEALTH} ---- DMG: {player.get_Damage()} ]")



def get_action():
    while True:
        ParseVerbs.list_available_verbs()
        action = input(f"[{player.get_Room().get_Room_Name().upper()}]: ").upper()
        ParseVerbs.check_verb(action)
        # action to move player in world 
        if action == "GO":
            move()
        elif action == "PICKUP":
            pick_up_items(player.get_Room()) 
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
    player.set_Name("Noble " + name)
    time.sleep(0.5)
    print("Hello " + player.get_Name() + ".")
    print("GAME STORYLINE START --------------------------------")
    time.sleep(0.5)
    print("enter BACK at any prompt to go back to the previous menu.")

    get_action() 
        

    GameEnd.end_of_game()