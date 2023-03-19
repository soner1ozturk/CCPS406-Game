from AssetBuilder import *
import Character
import GameStart
import GameEnd
import ParseVerbs
import time

def move():
    direction = input('Which direction to move? [N/S/E/W]: ')
    if player._getRoom().adjRooms[direction] != None:
        # updates player location and reprompts for next action
        newRoom = roomDict[player._getRoom().adjRooms[direction]]
        player._setRoom(newRoom)
        print(">  Entering the {new_room}...".format(new_room = newRoom._getRoomName()))
        get_action() 
    # no adj room in inputted direction
    else:
        print("There is nothing in that direction... ")
        move() 


def get_action():
    while True:
        ParseVerbs.list_available_verbs()
        verb = input("What To Do: ")
        verb.upper()
        ParseVerbs.check_verb(verb)
        # action to move player in world 
        if verb == "GO":
            move()

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