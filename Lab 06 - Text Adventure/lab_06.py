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
    room = Room()

    room.description = "You are in a stone hall with a circular marble table in the center." \
                       "Tapestries hang on the walls and there is a woven rug on the floor."
    room.north = 4
    room.south = None
    room.east = 2
    room.west = 0


main()