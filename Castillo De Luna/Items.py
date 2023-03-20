class Item:
    def __init__(self, id, name, firstMessage, secondMessage):
        self.id = id
        self.name = name
        self.firstMessage = firstMessage
        self.secondMessage = secondMessage
    
    def getName(self):
        return self.name.upper()
    
    def __repr__(self):
        return f'<Item: {self.name}>'

class Weapon(Item):
    def __init__(self, id, name, firstMessage, secondMessage, damage):
        super().__init__(id, name, firstMessage, secondMessage)
        self.damage = damage
    
    def isWeapon(self):
        return True 

    def isConsumable(self):
        return False

class Consumable(Item):
    def __init__(self, id, name, firstMessage, secondMessage, restoreHealth):
        super().__init__(id, name, firstMessage, secondMessage)
        self.restoreHealth = restoreHealth
    
    def isWeapon(self):
        return False 

    def isConsumable(self):
        return True