import arcade

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
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

        # Physics engine
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

        # Physics engine
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def on_draw(self):
        arcade.start_render()
        self.wall_list.draw()
        self.player_list.draw()

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