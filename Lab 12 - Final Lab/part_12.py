import arcade

SPRITE_SCALING = 0.5
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
NUMBER_OF_COINS = 5
MOVEMENT_SPEED = 5


class Room:

    def __init__(self):
        # Lists
        self.wall_list = None


def setup_room_1():
    """Room 1"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()

    # Walls, Room 1, image from https://kenney.nl
    for y in (0, SCREEN_HEIGHT - 16):
        for x in range(0, SCREEN_WIDTH, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    for y in range(0, 200, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = 0
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(300, SCREEN_HEIGHT, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = 0
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(0, 300, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = SCREEN_WIDTH
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(400, SCREEN_HEIGHT, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = SCREEN_WIDTH
        wall.center_y = y
        room.wall_list.append(wall)

    return room


def setup_room_2():
    """Room 2"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()

    # Walls, Room 2, image from https://kenney.nl
    for y in (0, SCREEN_HEIGHT - 16):
        for x in range(0, SCREEN_WIDTH, 32):
            wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    for y in range(0, 300, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = 0
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(400, SCREEN_HEIGHT, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = 0
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(0, 200, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = SCREEN_WIDTH
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(300, SCREEN_HEIGHT, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = SCREEN_WIDTH
        wall.center_y = y
        room.wall_list.append(wall)

    return room


def setup_room_3():
    """Room 3"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()

    # Walls, Room 3, image from https://kenney.nl
    for y in (0, SCREEN_HEIGHT - 16):
        for x in range(0, SCREEN_WIDTH, 32):
            wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    for y in range(0, 200, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = 0
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(300, SCREEN_HEIGHT, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = 0
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(0, 300, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = SCREEN_WIDTH
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(400, SCREEN_HEIGHT, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = SCREEN_WIDTH
        wall.center_y = y
        room.wall_list.append(wall)

    return room


def setup_room_4():
    """Room 4"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()

    # Walls, Room 4, image from https://kenney.nl
    for x in range(50, SCREEN_WIDTH, 63):
        wall = arcade.Sprite("waterTop_high.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 0
        room.wall_list.append(wall)

    for x in range(0, SCREEN_WIDTH, 63):
        wall = arcade.Sprite("waterTop_high.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = SCREEN_HEIGHT
        room.wall_list.append(wall)

    for y in range(0, 300, 63):
        wall = arcade.Sprite("water.png", SPRITE_SCALING)
        wall.center_x = 0
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(400, SCREEN_HEIGHT, 63):
        wall = arcade.Sprite("water.png", SPRITE_SCALING)
        wall.center_x = 0
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(0, 200, 63):
        wall = arcade.Sprite("water.png", SPRITE_SCALING)
        wall.center_x = SCREEN_WIDTH
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(300, SCREEN_HEIGHT, 63):
        wall = arcade.Sprite("water.png", SPRITE_SCALING)
        wall.center_x = SCREEN_WIDTH
        wall.center_y = y
        room.wall_list.append(wall)

    return room

def setup_room_5():
    """Room 5"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()

    # Walls, Room 5, image from https://kenney.nl
    for x in range(50, SCREEN_WIDTH, 63):
        wall = arcade.Sprite("lavaTop_high.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 0
        room.wall_list.append(wall)

    for x in range(0, SCREEN_WIDTH, 63):
        wall = arcade.Sprite("lavaTop_high.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = SCREEN_HEIGHT
        room.wall_list.append(wall)

    for y in range(0, 200, 63):
        wall = arcade.Sprite("lava.png", SPRITE_SCALING)
        wall.center_x = 0
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(300, SCREEN_HEIGHT, 63):
        wall = arcade.Sprite("lava.png", SPRITE_SCALING)
        wall.center_x = 0
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(0, 300, 63):
        wall = arcade.Sprite("lava.png", SPRITE_SCALING)
        wall.center_x = SCREEN_WIDTH
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(400, SCREEN_HEIGHT, 63):
        wall = arcade.Sprite("lava.png", SPRITE_SCALING)
        wall.center_x = SCREEN_WIDTH
        wall.center_y = y
        room.wall_list.append(wall)

    return room


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        """
        Initializer
        """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Sprite lists
        self.current_room = 0

        # Set up the player
        self.rooms = None
        self.player_sprite = None
        self.player_list = None
        self.physics_engine = None

    def setup(self):
        """ Set up the game and initialize the variables. """
        # Set up the player
        self.player_sprite = arcade.Sprite("player_05.png", SPRITE_SCALING)
        self.player_sprite.center_x = 0
        self.player_sprite.center_y = 250
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        # Our list of rooms
        self.rooms = []

        # Create the rooms. Extend the pattern for each room.
        room = setup_room_1()
        self.rooms.append(room)

        room = setup_room_2()
        self.rooms.append(room)

        room = setup_room_3()
        self.rooms.append(room)

        room = setup_room_4()
        self.rooms.append(room)

        room = setup_room_5()
        self.rooms.append(room)

        # Our starting room number
        self.current_room = 0

        # Create a physics engine for this room
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                         self.rooms[self.current_room].wall_list)
        # Reset the score
        self.score = 0

    def on_draw(self):
        """Render the screen."""
        self.clear()

        # Draw walls
        self.rooms[self.current_room].wall_list.draw()

        # If you have coins or monsters, then copy and modify the line
        # above for each list.

        self.player_list.draw()
        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.WHITE, 24)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.physics_engine.update()

        # Room logic
        if self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 0:
            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 0
        if self.player_sprite.center_x < 0 and self.current_room == 1:
            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = SCREEN_WIDTH
        if self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 1:
            self.current_room = 2
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 0
        if self.player_sprite.center_x < 0 and self.current_room == 1:
            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = SCREEN_WIDTH
        if self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 2:
            self.current_room = 3
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 0
        if self.player_sprite.center_x < 0 and self.current_room == 2:
            self.current_room = 2
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = SCREEN_WIDTH
        if self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 3:
            self.current_room = 4
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 0
        elif self.player_sprite.center_x < 0 and self.current_room == 3:
            self.current_room = 3
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = SCREEN_WIDTH


def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
