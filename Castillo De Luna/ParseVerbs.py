# go
# use
# quit
# pickup
# drop
# list
# inventory
# attack
# stats

def check_verb(verb):
    verbs = ["GO", "INV", "USE", "QUIT", "LIST", "STATS"]
    if verb in verbs:
        print("Good to do that: " + verb)
    else:
        print("Please enter a valid command... ")
        return False


def list_available_verbs():
    print("\n    [  GO  ]  [  INV  ] [  USE  ] [ LIST ] [ STATS ] [ QUIT ]\n")