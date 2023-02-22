class Room:
    """
    This is a class that describes the room.
    """
    def __init__(self):
        """Sets up the variables in the object."""
        self.description = ""
        self.north = ""
        self.south = ""
        self.east = ""
        self.west = ""


def main():
    room_list = [0, 1, 2, 3, 4, 5, 6]

    room1 = Room()
    room1.description = "You are in a stone hall. There are doors to the east and west."
    room1.north = None
    room1.south = None
    room1.east = 2
    room1.west = 0

    room2 = Room()
    room2.description = "You are in a room. There are doors to the north and west."
    room2.north = 5
    room2.south = None
    room2.east = None
    room2.west = 1

    room0 = Room()
    room0.description = "You are in a room. There are doors to the north and east."
    room0.north = 3
    room0.south = None
    room0.east = 1
    room0.west = None

    room3 = Room()
    room3.description = "You are in a room. There are doors to the south and east."
    room3.north = None
    room3.south = 0
    room3.east = 4
    room3.west = None

    room4 = Room()
    room4.description = "You are in a hall. There are doors to the east, west, north, and south."
    room4.north = 6
    room4.south = 1
    room4.east = 5
    room4.west = 3

    room5 = Room()
    room5.description = "You are in a room. There are doors to the west and south."
    room5.north = None
    room5.south = 2
    room5.east = None
    room5.west = 4

    room6 = Room()
    room6.description = "You are on a balcony. There is a door to the south."
    room6.north = None
    room6.south = 4
    room6.east = None
    room6.west = None






main()