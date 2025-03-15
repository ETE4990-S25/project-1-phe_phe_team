class Player:
    def __init__ (self,name,room = "Living Room", turn=0):
        self.name = name
        self.current_room = room
        self.turn_count = turn

class Neighbor(Player):
    def __init__(self,name):
        super().__init__(name, "Bedroom")
       # self.name = name
       # self.current_room = "Bedroom"
        self.move_count = 0

class Room:
    def __init__(self,name,conected_rooms):
        self.name = name
        self.conected_rooms = conected_rooms

class Mission:
    def __init__(self, description, room):
        self.description = description
        self.room = room
        self.completed = False
    
