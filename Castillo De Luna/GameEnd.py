def end_of_game():
    print("End Of The Game Message")

def end_of_game_conditions(badguy):
    if (badguy.get_health()<=0):
        print("You win")
