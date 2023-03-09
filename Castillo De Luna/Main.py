import AssetBuilder
import Character
import GameStart
import GameEnd
import ParseVerbs


if __name__ == "__main__":
    GameStart.start_of_game()

    gameData=AssetBuilder.load_data()
    print(gameData)

    name = input("Let's start with your name: ")
    print("Hello " + name + ".")
    player = Character.GoodCharacter(name)

    while True:
            ParseVerbs.list_available_verbs()
            verb=input("What To Do:")
            ParseVerbs.check_verb(verb)


            break



    GameEnd.end_of_game()