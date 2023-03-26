MAX_HEALTH = 100
DEFAULT_INVENTORY_SIZE = 3 


class Character:
    def __init__(self, id, name, health, damage):
        self.id = id
        self.name = name
        self.health = health
        self.damage = damage
        
    def get_Name(self):
        return self.name
    
    def set_Room(self, room):
        self.room = room
    
    def get_Room(self):
        return self.room
    
    def get_Health(self):
        return self.health

    def get_Damage(self):
        return self.damage
    
    def set_Health(self, hp):
        self.health = min(self.get_Health() + hp, MAX_HEALTH)

    def set_Damage(self, dmg):
        self.damage = min(dmg, MAX_HEALTH)
    
    def __repr__(self):
        return f'<Character: {self.name}>'

class GoodCharacter(Character): #sublcass, inherits from Character
    def __init__(self, id, name, health, damage):
        super().__init__(id, name, health, damage)
        self.inventory = []
        self.equipped = []
    
    def set_Name(self, name):
        self.name = name

    def get_Inv(self):
        return self.inventory
    
    def add_Item(self, item):
        self.inventory.append(item)

    def drop_Item(self, item):
        self.inventory.remove(item) 

    # returns adj rooms of room currently in 
    def get_AdjRooms(self):
        return self.room.adjRooms
    
    def add_Equip(self, item):
        self.equipped.append(item)
    def removeEquip(self, item):
        self.equipped.remove(item)
        
    def get_Equipped(self):
        return self.equipped

class BadCharacter(Character): #subclass, inherits from Character
    def __init__(self, id, name, health, damage):
        super().__init__(id, name, health, damage)