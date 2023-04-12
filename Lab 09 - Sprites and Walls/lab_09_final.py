import arcade
import random

SPRITE_SCALING = 0.5
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
NUMBER_OF_COINS = 50
MOVEMENT_SPEED = 5
CAMERA_SPEED = 1


class MyGame(arcade.Window):
    def __init__(self):
        """ Initializer """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Lists
        self.player_list = None
        self.wall_list = None
        self.coin_list = None

        # Player
        self.player_sprite = None

        # Sound
        self.laser_sound = arcade.load_sound("laser.wav")

        # Physics engine
        self.physics_engine = None

        # Cameras
        self.camera_for_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_for_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    def setup(self):
        arcade.set_background_color(arcade.color.BLACK)

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Reset the score
        self.score = 0

        # Image from https://kenney.nl
        self.player_sprite = arcade.Sprite("player_01.png", SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Walls, image from https://kenney.nl
        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 300
        wall.center_y = 200
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 550
        wall.center_y = 200
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 800
        wall.center_y = 200
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 150
        wall.center_y = 450
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 250
        wall.center_y = 450
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 200
        wall.center_y = 400
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 550
        wall.center_y = 350
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 450
        wall.center_y = 350
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 500
        wall.center_y = 400
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 800
        wall.center_y = 450
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 900
        wall.center_y = 450
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 850
        wall.center_y = 400
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 150
        wall.center_y = 650
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 200
        wall.center_y = 600
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 400
        wall.center_y = 550
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 450
        wall.center_y = 600
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 650
        wall.center_y = 650
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 700
        wall.center_y = 600
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 900
        wall.center_y = 550
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 950
        wall.center_y = 600
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 150
        wall.center_y = 750
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 250
        wall.center_y = 750
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 200
        wall.center_y = 800
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 550
        wall.center_y = 850
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 450
        wall.center_y = 850
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 500
        wall.center_y = 800
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 800
        wall.center_y = 450
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 900
        wall.center_y = 450
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 850
        wall.center_y = 400
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 800
        wall.center_y = 750
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 700
        wall.center_y = 750
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 750
        wall.center_y = 800
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 950
        wall.center_y = 850
        self.wall_list.append(wall)

        # Other walls, image from https://kenney.nl
        for x in range(100, 1100, 32):
            wall = arcade.Sprite("crate_01.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 100
            self.wall_list.append(wall)

        for x in range(10, 1000, 32):
            wall = arcade.Sprite("crate_01.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 300
            self.wall_list.append(wall)

        for x in range(100, 1100, 32):
            wall = arcade.Sprite("crate_01.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 500
            self.wall_list.append(wall)

        for x in range(10, 1000, 32):
            wall = arcade.Sprite("crate_01.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 700
            self.wall_list.append(wall)

        for x in range(100, 1120, 32):
            wall = arcade.Sprite("crate_01.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 900
            self.wall_list.append(wall)

        for y in range(100, 900, 32):
            wall = arcade.Sprite("crate_01.png", SPRITE_SCALING)
            wall.center_x = 10
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(100, 900, 32):
            wall = arcade.Sprite("crate_01.png", SPRITE_SCALING)
            wall.center_x = 1100
            wall.center_y = y
            self.wall_list.append(wall)

        # Coins, image from https://kenney.nl
        for i in range(NUMBER_OF_COINS):
            coin = arcade.Sprite("environment_11.png", SPRITE_SCALING)

            # Boolean variable coin placement
            coin_placed_successfully = False

            while not coin_placed_successfully:
                # Position the coin
                coin.center_x = random.randrange(SCREEN_WIDTH)
                coin.center_y = random.randrange(SCREEN_HEIGHT)
                coin.center_x = random.randrange(100, 1000)
                coin.center_y = random.randrange(100, 900)

                # See if the coin is hitting a wall
                wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)
                # See if the coin is hitting another coin
                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)
                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    # It is!
                    coin_placed_successfully = True
                # Add the coin to the lists
            self.coin_list.append(coin)

        # Physics engine
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def on_draw(self):
        arcade.start_render()

        # Scrolling camera for sprites
        self.camera_for_sprites.use()
        self.wall_list.draw()
        self.coin_list.draw()
        self.player_list.draw()

        # GUI camera
        self.camera_for_gui.use()
        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.WHITE, 24)

    def on_update(self, delta_time):
        """ Movement and game logic """
        # Update sprites
        self.physics_engine.update()
        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            arcade.play_sound(self.laser_sound)
            coin.remove_from_sprite_lists()
            self.score += 1

        # Scroll the window to the player.
        lower_left_corner = (self.player_sprite.center_x - self.width / 2,
                             self.player_sprite.center_y - self.height / 2)
        self.camera_for_sprites.move_to(lower_left_corner, CAMERA_SPEED)

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

    def update(self, delta_time):
        self.physics_engine.update()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
