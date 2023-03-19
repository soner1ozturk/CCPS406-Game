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
        self.inventory = ["apple", "orange", "banana", "orange"]
    
    def setName(self, name):
        self.name = name

    def _getInv(self):
        return self.inventory
    
    def _addInv(self, item):
        self.inventory.append(item)



class BadCharacter(Character): #subclass, inherits from Character
    def __init__(self, id, name, health):
        super().__init__(id, name, health)
