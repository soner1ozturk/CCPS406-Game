class Character:
    id = ''
    health = 100
    name=''

    def __init__(self, name):
        self.name = name

class GoodCharacter(Character): #sublcass, inherits from Character
    def getname(self):
        return self.name

class BadCharacter(Character): #subclass, inherits from Character
    def getname(self):
        return self.name