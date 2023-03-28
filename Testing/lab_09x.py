import random
import arcade
import pyglet.math
import Vec2

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
        self.player_sprite = arcade.Sprite("../Lab 09 - Sprites and Walls/player_01.png",
                                           scale=0.5)
        self.player_sprite.center_x = 450
        self.player_sprite.center_y = 250
        self.player_list.append(self.player_sprite)

        for x in range(200, 1650, 210):
            for y in range(0, 1600, 64):
                # Image from https://kenney.nl
                if random.randrange(5) > 0:
                    wall = arcade.Sprite("../Lab 09 - Sprites and Walls/crate_01.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.DARK_MIDNIGHT_BLUE)

    def on_draw(self):
        # Render
        self.clear()

        self.camera_sprites.use()

        self.wall_list.draw()
        self.player_list.draw()

        self.camera_gui.use()

        # GUI
        arcade.draw_rectangle_filled(self.width // 2,
                                     20,
                                     self.width,
                                     40,
                                     arcade.color.ORANGE)
        text = f"Scroll value: ({self.camera_sprites.position[0]:5.1f}, " \
               f"{self.camera_sprites.position[1]:5.1f})"
        arcade.draw_text(text, 10, 10, arcade.color.RED, 20)

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
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

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
