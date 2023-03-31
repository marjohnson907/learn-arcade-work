import random
import arcade
from pyglet.math import Vec2

SPRITE_SCALING = 0.5
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MARGIN = 25
CAMERA_SPEED = 1
MOVEMENT_SPEED = 5


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
        self.score = 0

        # Image from https://kenney.nl
        self.player_sprite = arcade.Sprite("player_01.png", SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 75
        self.player_list.append(self.player_sprite)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Image from https://kenney.nl
        for x in range(100, 1000, 32):
            wall = arcade.Sprite("crate_01.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 100
            self.wall_list.append(wall)

        for x in range(100, 1000, 32):
            wall = arcade.Sprite("crate_01.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 300
            self.wall_list.append(wall)

        for x in range(100, 1000, 32):
            wall = arcade.Sprite("crate_01.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 500
            self.wall_list.append(wall)

        for x in range(100, 1000, 32):
            wall = arcade.Sprite("crate_01.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 700
            self.wall_list.append(wall)

        for x in range(100, 1000, 32):
            wall = arcade.Sprite("crate_01.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 900
            self.wall_list.append(wall)

        for x in range(100, 1000, 32):
            wall = arcade.Sprite("crate_01.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 1100
            self.wall_list.append(wall)

        # Image from https://kenney.nl
        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 300
        wall.center_y = 200
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 600
        wall.center_y = 200
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 800
        wall.center_y = 200
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 200
        wall.center_y = 400
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 300
        wall.center_y = 400
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 500
        wall.center_y = 400
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 700
        wall.center_y = 400
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 800
        wall.center_y = 400
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 200
        wall.center_y = 550
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 200
        wall.center_y = 650
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 400
        wall.center_y = 600
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 600
        wall.center_y = 550
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 600
        wall.center_y = 650
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 950
        wall.center_y = 550
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 950
        wall.center_y = 650
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 800
        wall.center_y = 600
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 500
        wall.center_y = 800
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 450
        wall.center_y = 750
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 550
        wall.center_y = 750
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 800
        wall.center_y = 850
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 900
        wall.center_y = 850
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
        wall.center_x = 850
        wall.center_y = 800
        self.wall_list.append(wall)

        for x in range(150, 1000, 200):
            wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 950
            self.wall_list.append(wall)

        for x in range(200, 900, 200):
            wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 1050
            self.wall_list.append(wall)

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        # Render
        self.clear()

        self.camera_sprites.use()

        self.wall_list.draw()
        self.player_list.draw()

        self.camera_gui.use()

        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.WHITE, 24)

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

    def on_update(self, delta_time):
        # Movement & game logic
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = MOVEMENT_SPEED

        self.physics_engine.update()

        self.scroll_to_player()

    def scroll_to_player(self):

        position = Vec2(self.player_sprite.center_x - self.width / 2,

                        self.player_sprite.center_y - self.height / 2)

        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):

        self.camera_sprites.resize(int(width), int(height))

        self.camera_gui.resize(int(width), int(height))


def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
