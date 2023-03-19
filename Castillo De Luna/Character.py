class Character:
    def __init__(self, id, name, health):
        self.id = id
        self.name = name
        self.health = health
 
    def getName(self):
        return self.name
    
    def _setRoom(self, room):
        self.room = room
    
    def _getRoom(self):
        return self.room


    def __repr__(self):
        return f'<Character: {self.name}>'

class GoodCharacter(Character): #sublcass, inherits from Character
    def __init__(self, id, name, health):
        super().__init__(id, name, health)
        self.room = None
        self.inventory = []
    
    def setName(self, name):
        self.name = name
    


class BadCharacter(Character): #subclass, inherits from Character
    def __init__(self, id, name, health):
        super().__init__(id, name, health)
        self.room = None
