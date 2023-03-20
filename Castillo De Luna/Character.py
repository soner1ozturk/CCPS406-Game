MAX_HEALTH = 100

class Character:
    def __init__(self, id, name, health, damage):
        self.id = id
        self.name = name
        self.health = health
        self.damage = damage
        
    def getName(self):
        return self.name
    
    def _setRoom(self, room):
        self.room = room
    
    def _getRoom(self):
        return self.room
    
    def _getHealth(self):
        return self.health

    
    def __repr__(self):
        return f'<Character: {self.name}>'

class GoodCharacter(Character): #sublcass, inherits from Character
    def __init__(self, id, name, health, damage):
        super().__init__(id, name, health, damage)
        self.inventory = []
    
    def setName(self, name):
        self.name = name

    def _getInv(self):
        return self.inventory
    
    def _addInv(self, item):
        self.inventory.append(item)

    def _remInv(self, item):
        self.inventory.remove(item)


class BadCharacter(Character): #subclass, inherits from Character
    def __init__(self, id, name, health, damage):
        super().__init__(id, name, health, damage)
