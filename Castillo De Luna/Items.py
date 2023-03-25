class Item:
    def __init__(self, id: int, name: str, firstMessage: str, secondMessage: str):
        self.id = id
        self.name = name
        self.firstMessage = firstMessage
        self.secondMessage = secondMessage
    
    def getName(self):
        return self.name.upper()
    
    def __repr__(self):
        return f'<Item: {self.name}>'

class Weapon(Item):
    def __init__(self, id: int, name: str, first_message: str, second_message: str, damage: int):
        super().__init__(id, name, first_message, second_message)
        self.damage = damage
    
    def isWeapon(self):
        return True 

    def isConsumable(self):
        return False

class Consumable(Item):
    def __init__(self, id: int, name: str, first_message: str, second_message: str, restore_health: int):
        super().__init__(id, name, first_message, second_message)
        self.restoreHealth = restore_health
    
    def isWeapon(self):
        return False 

    def isConsumable(self):
        return True