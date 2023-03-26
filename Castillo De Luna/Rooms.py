
class Room:
    def __init__(self, id, name, visited, adjRooms, firstMessage, secondMessage):
        self.id = id
        self.name = name
        self.visited = visited
        self.adjRooms = adjRooms
        self.firstMessage = firstMessage
        self.secondMessage = secondMessage
        self.itemsInRoom=[]

    def __repr__(self):
        return f'<Room: {self.name}>'

    def getRoomName(self):
        return self.name

    def getItemsInRoom(self):
        return self.itemsInRoom

    def addItemInRoom(self, item):
        self.itemsInRoom.append(item)

    def removeItemInRoom(self, item):
        self.itemsInRoom.remove(item)

    def getRoomMessage(self):
        print(self.firstMessage)
        self.firstMessage=self.secondMessage