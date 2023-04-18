import arcade
import random

SPRITE_SCALING = 0.5
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
NUMBER_OF_COINS = 10
NUMBER_OF_STARS = 5
MOVEMENT_SPEED = 5


class Room:

    def __init__(self):
        # Lists
        self.wall_list = None
        self.coin_list = None
        self.star_list = None


def setup_room_1():
    """Room 1"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.coin_list = arcade.SpriteList()
    room.star_list = arcade.SpriteList()

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

        # Coins, image from https://kenney.nl
        for i in range(NUMBER_OF_COINS):
            coin = arcade.Sprite("coinGold.png", SPRITE_SCALING/2)

            # Boolean variable coin placement
            coin_placed_successfully = False

            while not coin_placed_successfully:
                # Position the coin
                coin.center_x = random.randrange(SCREEN_WIDTH - 25)
                coin.center_y = random.randrange(SCREEN_HEIGHT - 25)

                # See if the coin is hitting a wall
                wall_hit_list = arcade.check_for_collision_with_list(coin, room.wall_list)
                # See if the coin is hitting another coin
                coin_hit_list = arcade.check_for_collision_with_list(coin, room.coin_list)
                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    # It is!
                    coin_placed_successfully = True
            # Add the coin to the lists
            room.coin_list.append(coin)

    return room


def setup_room_2():
    """Room 2"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.coin_list = arcade.SpriteList()
    room.star_list = arcade.SpriteList()

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

    # Coins, image from https://kenney.nl
    for i in range(NUMBER_OF_COINS):
        coin = arcade.Sprite("coinSilver.png", SPRITE_SCALING / 2)

        # Boolean variable coin placement
        coin_placed_successfully = False

        while not coin_placed_successfully:
            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH - 25)
            coin.center_y = random.randrange(SCREEN_HEIGHT - 25)

            # See if the coin is hitting a wall
            wall_hit_list = arcade.check_for_collision_with_list(coin, room.wall_list)
            # See if the coin is hitting another coin
            coin_hit_list = arcade.check_for_collision_with_list(coin, room.coin_list)
            if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                # It is!
                coin_placed_successfully = True
        # Add the coin to the lists
        room.coin_list.append(coin)

        # Stars, image from https://kenney.nl
        for i in range(NUMBER_OF_STARS):
            star = arcade.Sprite("star.png", SPRITE_SCALING / 2)

            # Boolean variable star placement
            star_placed_successfully = False

            while not star_placed_successfully:
                # Position the stars
                star.center_x = random.randrange(SCREEN_WIDTH - 25)
                star.center_y = random.randrange(SCREEN_HEIGHT - 25)

                # See if the star is hitting a wall
                wall_hit_list = arcade.check_for_collision_with_list(star, room.wall_list)
                # See if the star is hitting another star or coin
                star_hit_list = arcade.check_for_collision_with_list(coin, room.coin_list, room.star_list)
                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    # It is!
                    star_placed_successfully = True
            # Add the star to the lists
            room.star_list.append(star)

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
        # Sound
        self.laser_sound = arcade.load_sound("laser.wav")
        self.player_list = None
        self.coin_list = None
        self.star_list = None
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

        # Draw coins
        self.rooms[self.current_room].coin_list.draw()

        # Draw stars
        self.rooms[self.current_room].star_list.draw()

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

        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.rooms[self.current_room].coin_list)
        star_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.rooms[self.current_room].star_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            arcade.play_sound(self.laser_sound)
            coin.remove_from_sprite_lists()
            self.score += 1
        for star in star_hit_list:
            arcade.play_sound(self.laser_sound)
            star.remove_from_sprite_lists()
            self.score += 5

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
