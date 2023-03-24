
MAX_HEALTH = 100
DEFAULT_INVENTORY_SIZE = 3 


class Character:
    def __init__(self, id: int, name: str, health: int, damage: int):
        self.id = id
        self.name = name
        self.health = health
        self.damage = damage
        
    def getName(self):
        return self.name
    
    def setRoom(self, room):
        self.room = room
    
    def getRoom(self):
        return self.room
    
    def getHealth(self):
        return self.health

    def getDamage(self):
        return self.damage
    
    def setHealth(self, hp):
        self.health = min(self.getHealth() + hp, MAX_HEALTH)

    def setDamage(self, dmg):
        self.damage = min(self.getDamage() + dmg, MAX_HEALTH)
    
    def __repr__(self):
        return f'<Character: {self.name}>'

class GoodCharacter(Character): #subclass, inherits from Character
    def __init__(self, id: int, name: str, health: int, damage: int):
        super().__init__(id, name, health, damage)
        self.inventory = []
        self.equipped = []
    
    def setName(self, name):
        self.name = name

    def getInv(self):
        return self.inventory
    
    def addItem(self, item):
        self.inventory.append(item)

    def dropItem(self, item):
        self.inventory.remove(item) 

    # returns adj rooms of room currently in 
    def getAdjRooms(self):
        return self.room.adjRooms
    
    def addEquip(self, item):
        self.equipped.append(item)

    def getEquipped(self):
        return self.equipped
    




class BadCharacter(Character): #subclass, inherits from Character
    def __init__(self, id: int, name: str, health: int, damage: int):
        super().__init__(id, name, health, damage)
