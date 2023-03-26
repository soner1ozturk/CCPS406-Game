
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

    def get_Room_Name(self):
        return self.name

    def get_Items_In_Room(self):
        return self.itemsInRoom

    def add_Item_In_Room(self, item):
        self.itemsInRoom.append(item)

    def remove_Item_In_Room(self, item):
        self.itemsInRoom.remove(item)

    def get_Room_Message(self):
        print(self.firstMessage)
        self.firstMessage=self.secondMessage