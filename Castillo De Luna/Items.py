class Item:
    def __init__(self, id, name, firstMessage, secondMessage):
        self.id = id
        self.name = name
        self.firstMessage = firstMessage
        self.secondMessage = secondMessage

    def __repr__(self):
        return f'<Item: {self.name}>'

class Weapon(Item):
    def __init__(self, id, name, firstMessage, secondMessage, damage):
        super().__init__(id, name, firstMessage, secondMessage)
        self.damage = damage

class Consumable(Item):
    def __init__(self, id, name, firstMessage, secondMessage, restoreHealth):
        super().__init__(id, name, firstMessage, secondMessage)
        self.restoreHealth = restoreHealth