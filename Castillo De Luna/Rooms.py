
class Room:
    def __init__(self, id: int, name: str, visited: bool, adj_rooms: list, first_message: str, second_message: str):
        self.id = id
        self.name = name
        self.visited = visited
        self.adjRooms = adj_rooms
        self.firstMessage = first_message
        self.secondMessage = second_message
        self.itemsInRoom=[]

    def getRoomName(self):
        return self.name

    def __repr__(self):
        return f'<Room: {self.name}>'
    
    def getItemsInRoom(self):
        return self.itemsInRoom

    def addItemInRoom(self, item):
        self.itemsInRoom.append(item)

    def removeItemInRoom(self, item):
        self.itemsInRoom.remove(item)
