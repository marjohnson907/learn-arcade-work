
import random
import arcade

SPRITE_SCALING = 0.5
BLOB_COUNT = 50

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 8")

        self.player_list = None
        self.blob_list = None

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.EERIE_BLACK)

    def setup(self):

        self.player_list = arcade.SpriteList()
        self.blob_list = arcade.SpriteList()

        self.score = 0

        self.player_sprite = arcade.Sprite("alienBlue_front.png", SPRITE_SCALING)
        self.player_sprite.center_x = 350
        self.player_sprite.center_y = 350
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        arcade.start_render()


def main():
    window = MyGame
    arcade.run()


if __name__ == "__main__":
    main()
