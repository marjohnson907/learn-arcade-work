import arcade

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):

    def __init__(self):
        """ Initializer """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Lists
        self.player_list = None
        self.wall_list = None

        # Player
        self.player_sprite = None

        self.physics_engine = None

    def setup(self):
        arcade.set_background_color(arcade.color.BLACK)

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Reset the score
        self.score = 0

        # Image from https://kenney.nl
        self.player_sprite = arcade.Sprite("player_01.png", SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        arcade.start_render()
        self.wall_list.draw()
        self.player_list.draw()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()