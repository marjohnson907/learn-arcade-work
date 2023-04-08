import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SPRITE_SCALING = 0.5
NUMBER_OF_COINS = 50
MOVEMENT_SPEED = 5
CAMERA_SPEED = 1


class MyGame(arcade.Window):
    def __init__(self):
        """Initializer"""
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Lists
        self.player_list = None
        self.wall_list = None
        self.coin_list = None

        # Player
        self.player_sprite = None

        # Sound

        # Physics engine
        self.physics_engine = None

        # Cameras
        self.camera_for_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_for_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        arcade.set_background_color(arcade.color.AUROMETALSAURUS)
        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Reset the score
        self.score = 0

        # Image from https://kenney.nl
        self.player_sprite = arcade.Sprite("player_05.png", SPRITE_SCALING)
        self.player_sprite.center_x = 10
        self.player_sprite.center_y = 10
        self.player_list.append(self.player_sprite)

        # Brick, Room 1, image from https://kenney.nl
        for x in range(50, 1550, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 50
            self.wall_list.append(wall)

        for x in range(350, 550, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 150
            self.wall_list.append(wall)

        for x in range(950, 1350, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 150
            self.wall_list.append(wall)

        for x in range(1450, 1550, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 150
            self.wall_list.append(wall)

        for x in range(50, 350, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 250
            self.wall_list.append(wall)

        for x in range(550, 950, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 250
            self.wall_list.append(wall)

        for x in range(1150, 1450, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 250
            self.wall_list.append(wall)

        for x in range(150, 750, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 350
            self.wall_list.append(wall)

        for x in range(950, 1350, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 350
            self.wall_list.append(wall)

        for x in range(550, 950, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 450
            self.wall_list.append(wall)

        for x in range(1250, 1450, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 450
            self.wall_list.append(wall)

        for x in range(750, 850, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 550
            self.wall_list.append(wall)

        for x in range(450, 650, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 550
            self.wall_list.append(wall)

        for x in range(1150, 1350, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 550
            self.wall_list.append(wall)

        for x in range(1450, 1550, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 550
            self.wall_list.append(wall)

        for x in range(150, 350, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 650
            self.wall_list.append(wall)

        for x in range(650, 950, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 650
            self.wall_list.append(wall)

        for x in range(1050, 1250, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 650
            self.wall_list.append(wall)

        for x in range(1350, 1550, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 650
            self.wall_list.append(wall)

        for x in range(150, 450, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 750
            self.wall_list.append(wall)

        for x in range(550, 650, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 750
            self.wall_list.append(wall)

        for x in range(750, 850, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 750
            self.wall_list.append(wall)

        for x in range(950, 1050, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 750
            self.wall_list.append(wall)

        for x in range(1150, 1450, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 750
            self.wall_list.append(wall)

        for x in range(250, 350, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 850
            self.wall_list.append(wall)

        for x in range(650, 950, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 850
            self.wall_list.append(wall)

        for x in range(1050, 1150, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 850
            self.wall_list.append(wall)

        for x in range(1250, 1350, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 850
            self.wall_list.append(wall)

        for x in range(50, 250, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 950
            self.wall_list.append(wall)

        for x in range(350, 750, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 950
            self.wall_list.append(wall)

        for x in range(950, 1150, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 950
            self.wall_list.append(wall)

        for x in range(1350, 1450, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 950
            self.wall_list.append(wall)

        for x in range(50, 1550, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 1050
            self.wall_list.append(wall)

        for y in range(50, 450, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = 50
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(550, 1050, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = 50
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(50, 150, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = 150
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(350, 550, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = 150
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(750, 850, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = 150
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(150, 250, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = 250
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(450, 650, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = 250
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(850, 950, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = 250
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(50, 150, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = 350
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(350, 650, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = 350
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(150, 350, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = 450
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(450, 950, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = 450
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(350, 450, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = 550
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(650, 950, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = 550
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(50, 250, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = 650
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(550, 650, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = 650
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(50, 150, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = 750
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(750, 850, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = 750
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(150, 250, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = 850
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(350, 550, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = 850
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(850, 1050, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = 850
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(50, 150, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = 950
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(550, 850, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = 950
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(150, 250, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = 1050
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(350, 650, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = 1050
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(450, 550, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = 1150
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(750, 950, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = 1150
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(350, 450, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = 1250
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(850, 1050, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = 1250
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(550, 650, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = 1350
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(250, 550, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = 1450
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(750, 950, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = 1450
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(50, 550, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = 1550
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(650, 1050, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.center_x = 1550
            wall.center_y = y
            self.wall_list.append(wall)

        # Coins, image from https://kenney.nl
        """for i in range(NUMBER_OF_COINS):
            coin = arcade.Sprite("coin_01.png", SPRITE_SCALING/4)

            # Boolean variable coin placement
            coin_placed_successfully = False

            while not coin_placed_successfully:
                # Position the coin
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
            self.coin_list.append(coin)"""

        # Physics engine
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def on_draw(self):
        # Render the screen.
        arcade.start_render()

        # Scrolling camera for sprites
        self.camera_for_sprites.use()

        self.wall_list.draw()
        self.coin_list.draw()
        self.player_list.draw()

        # GUI camera
        self.camera_for_gui.use()
        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.BLACK, 24)

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
