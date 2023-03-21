

MAX_HEALTH = 100

class Character:
    def __init__(self, id, name, health, damage):
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

class GoodCharacter(Character): #sublcass, inherits from Character
    def __init__(self, id, name, health, damage):
        super().__init__(id, name, health, damage)
        self.inventory = []
        self.equipped = []
    
    def setName(self, name):
        self.name = name

    def getInv(self):
        return self.inventory
    
    def addInv(self, item):
        self.inventory.append(item)

    def remInv(self, item):
        self.inventory.remove(item)
    # returns adj rooms of room currently in 
    def getAdjRooms(self):
        return self.room.adjRooms
    
    def addEquip(self, item):
        self.equipped.append(item)

    def getEquipped(self):
        return self.equipped
    




class BadCharacter(Character): #subclass, inherits from Character
    def __init__(self, id, name, health, damage):
        super().__init__(id, name, health, damage)
