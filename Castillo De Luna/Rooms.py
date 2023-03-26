
class Room:
    def __init__(self, id, name, visited, adjRooms, firstMessage, secondMessage):
        self.id = id
        self.name = name
        self.visited = visited
        self.adjRooms = adjRooms
        self.firstMessage = firstMessage
        self.secondMessage = secondMessage
        self.items_in_room=[]

    def __repr__(self):
        return f'<Room: {self.name}>'

    def get_room_name(self):
        return self.name

    def get_items_in_rooms(self):
        return self.items_in_room

    def add_Item_In_Room(self, item):
        self.items_in_room.append(item)

    def remove_Item_In_Room(self, item):
        self.items_in_room.remove(item)

    def get_room_message(self):
        if self.visited:
            print(self.secondMessage)
        else:
            self.visited=True
            print(self.firstMessage)