class Room:
    """
    This is a class that describes the room.
    """
    def __init__(self):
        """Sets up the variables in the object."""
        self.description = ""
        self.north = 0
        self.south = 0
        self.east = 0
        self.west = 0


def main():
    room_list = []

    room = Room()
    room.description = "You are in a room. There are doors to the north and east."
    room.north = 3
    room.south = None
    room.east = 1
    room.west = None
    room_list.append(room)

    room = Room()
    room.description = "You are in a stone hall. There are doors to the east and west."
    room.north = None
    room.south = None
    room.east = 2
    room.west = 0
    room_list.append(room)

    room = Room()
    room.description = "You are in a room. There are doors to the north and west."
    room.north = 5
    room.south = None
    room.east = None
    room.west = 1
    room_list.append(room)

    room = Room()
    room.description = "You are in a room. There are doors to the south and east."
    room.north = None
    room.south = 0
    room.east = 4
    room.west = None
    room_list.append(room)

    room = Room()
    room.description = "You are in a hall. There are doors to the east, west, north, and south."
    room.north = 6
    room.south = 1
    room.east = 5
    room.west = 3
    room_list.append(room)

    room = Room()
    room.description = "You are in a room. There are doors to the west and south."
    room.north = None
    room.south = 2
    room.east = None
    room.west = 4
    room_list.append(room)

    room = Room()
    room.description = "You are on a balcony. There is a door to the south."
    room.north = None
    room.south = 4
    room.east = None
    room.west = None
    room_list.append(room)

    current_room = 0

    done = False

    while not done:
        print(" ")
        print(room_list[current_room].description)

        user_choice = input("Where do you want to go?")

        # if user chooses north
        if user_choice.lower() == "n" or user_choice.lower() == "north":
            next_room = room_list[current_room].north
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # if user chooses south
        elif user_choice.lower() == "s" or user_choice.lower() == "south":
            next_room = room_list[current_room].south
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # if user chooses east
        elif user_choice.lower() == "e" or user_choice.lower() == "east":
            next_room = room_list[current_room].east
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # if user chooses west
        elif user_choice.lower() == "w" or user_choice.lower() == "west":
            next_room = room_list[current_room].west
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # to quit
        elif user_choice.upper() == "Q" or user_choice.upper() == "QUIT":
            print("You have quit.")
            done = True

        # if user enters another selection
        else:
            print("That is not a valid input.")


if __name__ == "__main__":
    main()