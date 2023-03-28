import random
import arcade
# import pyglet.math
# import Vec2

SPRITE_SCALING = 1
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 550
MARGIN = 100
CAMERA_SPEED = 0.1
PLAYER_MOVEMENT_SPEED = 1


class MyGame(arcade.Window):
    def __init__(self, width, height):

        super().__init__(width, height, resizable=True)

        self.player_list = None
        self.wall_list = None

        self.player_sprite = None

        self.physics_engine = None

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        self.camera_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.camera_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    def setup(self):
        # Game play
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Image from https://kenney.nl
        self.player_sprite = arcade.Sprite("player_01.png",
                                           scale=0.5)
        self.player_sprite.center_x = 450
        self.player_sprite.center_y = 250
        self.player_list.append(self.player_sprite)

        for x in range(200, 1650, 210):
            for y in range(0, 1600, 64):
                # Image from https://kenney.nl
                if random.randrange(5) > 0:
                    wall = arcade.Sprite("crate_01.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)