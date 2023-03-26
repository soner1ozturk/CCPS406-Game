

MAX_HEALTH = 100
DEFAULT_INVENTORY_SIZE = 3 


class Character:
    def __init__(self, id, name, health, damage):
        self.room = None
        self.id = id
        self.name = name
        self.health = health
        self.damage = damage
        
    def get_name(self):
        return self.name
    
    def set_room(self, room):
        self.room = room
    
    def get_room(self):
        return self.room
    
    def get_health(self):
        return self.health

    def get_damage(self):
        return self.damage
    
    def set_health(self, hp):
        self.health = min(hp, MAX_HEALTH)

    def set_damage(self, dmg):
        self.damage = min(dmg, MAX_HEALTH)
    
    def __repr__(self):
        return f'<Character: {self.name}>'

class GoodCharacter(Character): #sublcass, inherits from Character
    def __init__(self, id, name, health, damage):
        super().__init__(id, name, health, damage)
        self.inventory = []
        self.equipped = []
    
    def set_name(self, name):
        self.name = name

    def get_inv(self):
        return self.inventory
    
    def add_item(self, item):
        self.inventory.append(item)

    def drop_item(self, item):
        self.inventory.remove(item) 

    # returns adj rooms of room currently in 
    def get_adj_rooms(self):
        return self.room.adjRooms
    
    def add_equip(self, item):
        self.equipped.append(item)

    def remove_equip(self, item):
        self.equipped.remove(item)

    def get_equipped(self):
        return self.equipped

class BadCharacter(Character): #subclass, inherits from Character
    def __init__(self, id, name, health, damage):
        super().__init__(id, name, health, damage)
