import arcade
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

SPRITE_SCALING = 0.5
NUMBER_OF_COINS = 50
MOVEMENT_SPEED = 5
CAMERA_SPEED = 1


class Room:
    """Room information"""
    def __init__(self):

        self.wall_list = None
        self.coin_list = None


def setup_room_2():
    """Room 2"""
    room = Room()
    arcade.set_background_color(arcade.color.GREEN)

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.coin_list = arcade.SpriteList()

    # Walls, Room 2, image from https://kenney.nl


    return room


class MyGame(arcade.Window):
    """Main application class."""
    def __init__(self):
        """Initializer"""
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Sprite Lists
        self.current_room = 0
        self.player_sprite = None
        self.player_list = None

        # Sound
        self.laser_sound = arcade.load_sound("laser.wav")

        # Physics engine
        self.physics_engine = None

        # Cameras
        self.camera_for_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_for_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """

        # Reset the score
        self.score = 0

        # Player, image from https://kenney.nl
        self.player_sprite = arcade.Sprite("player_05.png", SPRITE_SCALING)
        self.player_sprite.center_x = 10
        self.player_sprite.center_y = 500
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        # Rooms list
        self.rooms = []

        # Create rooms
        room = setup_room_2()
        self.rooms.append(room)

        # Starting room number
        self.current_room = 0

        # Physics engine
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)

    def on_draw(self):
        # Render the screen.
        self.clear()
        # Draw walls
        self.rooms[self.current_room].wall_list.draw()
        # Draw coins

        # Draw player
        self.player_list.draw()

        # Scrolling camera for sprites
        self.camera_for_sprites.use()

        # GUI camera
        self.camera_for_gui.use()
        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.BLACK, 24)

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Update sprites
        self.physics_engine.update()

        """# Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            arcade.play_sound(self.laser_sound)
            coin.remove_from_sprite_lists()
            self.score += 1"""

        # Scroll the window to the player.
        lower_left_corner = (self.player_sprite.center_x - self.width / 2,
                             self.player_sprite.center_y - self.height / 2)
        self.camera_for_sprites.move_to(lower_left_corner, CAMERA_SPEED)

        # Room logic
        if self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 0:
            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 0
        elif self.player_sprite.center_x < 0 and self.current_room == 1:
            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = SCREEN_WIDTH

    def on_key_press(self, key, key_modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, key_modifiers):
        """Called when the user releases a key. """
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def update(self, delta_time):
        self.physics_engine.update()


def main():
    """ Main function """
    game = MyGame()
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
