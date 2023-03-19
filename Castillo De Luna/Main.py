from AssetBuilder import *
import Character
import GameStart
import GameEnd
import ParseVerbs
import time


if __name__ == "__main__":
    GameStart.start_of_game()
    name = input("Let's start with your name: ")
    player.setName(name)
    time.sleep(1)
    print("Hello " + player.getName() + ".")
    print("GAME STORYLINE START --------------------------------")
    time.sleep(1)
    

    while True:
            ParseVerbs.list_available_verbs()
            verb=input("What To Do: ")
            ParseVerbs.check_verb(verb)


            break



    GameEnd.end_of_game()