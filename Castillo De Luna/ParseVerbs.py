# go
# use
# quit
# pickup
# drop
# list
# inventory
# attack

def check_verb(verb):
    verbs = ["GO", "USE", "QUIT", "LIST"]
    if verb in verbs:
        print("Good to do that: " + verb)
    else:
        print("Please enter a valid command... ")
        return False

def list_available_verbs():
    print(" GO |  USE  |  QUIT  | LIST ")