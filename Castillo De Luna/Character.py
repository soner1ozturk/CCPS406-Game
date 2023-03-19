class Character:
    def __init__(self, id, name, health):
        self.id = id
        self.name = name
        self.health = health

    def getName(self):
        return self.name
    

    
    def __repr__(self):
        return f'<Character: {self.name}>'

class GoodCharacter(Character): #sublcass, inherits from Character
    def __init__(self, id, name, health):
        super().__init__(id, name, health)
        self.inventory = []
    
    def setName(self, name):
        self.name = name



class BadCharacter(Character): #subclass, inherits from Character
    def __init__(self, id, name, health):
        super().__init__(id, name, health)
