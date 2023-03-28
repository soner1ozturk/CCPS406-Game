class Room:
    def __init__(self, id: int, name: str, visited: bool, adjRooms: list, firstMessage: str, secondMessage: str):
        self.id = id
        self.name = name
        self.visited = visited
        self.adj_rooms = adjRooms
        self.firstMessage = firstMessage
        self.secondMessage = secondMessage
        self.items_in_room=[]

    def __repr__(self):
        return f'<Room: {self.name}>'

    def get_room_name(self):
        return self.name

    def get_items_in_room(self):
        return self.items_in_room

    def add_item_in_room(self, item):
        self.items_in_room.append(item)

    def remove_item_in_room(self, item):
        self.items_in_room.remove(item)

    def get_room_message(self):
        if self.visited:
            print(self.secondMessage)
        else:
            self.visited=True
            print(self.firstMessage)