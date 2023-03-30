import arcade

SPRITE_SCALING_BOX = 0.5
SPRITE_SCALING_PLAYER = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 5
CAMERA_SPEED = 1


class MyGame(arcade.Window):

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.player_list = None
        self.wall_list = None

        self.player_sprite = None

        self.physics_engine = None

        self.camera_for_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_for_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    def setup(self):
        arcade.set_background_color(arcade.color.BLACK)

        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        self.score = 0

        # Image from https://kenney.nl
        self.player_sprite = arcade.Sprite("player_01.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 75
        self.player_list.append(self.player_sprite)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Image from https://kenney.nl
        for x in range(100, 1000, 32):
            wall = arcade.Sprite("crate_01.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 100
            self.wall_list.append(wall)

        for x in range(100, 1000, 32):
            wall = arcade.Sprite("crate_01.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 300
            self.wall_list.append(wall)

        for x in range(100, 1000, 32):
            wall = arcade.Sprite("crate_01.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 500
            self.wall_list.append(wall)

        for x in range(100, 1000, 32):
            wall = arcade.Sprite("crate_01.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 700
            self.wall_list.append(wall)

        for x in range(100, 1000, 32):
            wall = arcade.Sprite("crate_01.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 900
            self.wall_list.append(wall)

        for x in range(100, 1000, 32):
            wall = arcade.Sprite("crate_01.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 1100
            self.wall_list.append(wall)

        # Image from https://kenney.nl
        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING_BOX)
        wall.center_x = 300
        wall.center_y = 200
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING_BOX)
        wall.center_x = 600
        wall.center_y = 200
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING_BOX)
        wall.center_x = 800
        wall.center_y = 200
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING_BOX)
        wall.center_x = 200
        wall.center_y = 400
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING_BOX)
        wall.center_x = 300
        wall.center_y = 400
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING_BOX)
        wall.center_x = 500
        wall.center_y = 400
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING_BOX)
        wall.center_x = 700
        wall.center_y = 400
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING_BOX)
        wall.center_x = 800
        wall.center_y = 400
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING_BOX)
        wall.center_x = 200
        wall.center_y = 550
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING_BOX)
        wall.center_x = 200
        wall.center_y = 650
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING_BOX)
        wall.center_x = 400
        wall.center_y = 600
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING_BOX)
        wall.center_x = 600
        wall.center_y = 550
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING_BOX)
        wall.center_x = 600
        wall.center_y = 650
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING_BOX)
        wall.center_x = 950
        wall.center_y = 550
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING_BOX)
        wall.center_x = 950
        wall.center_y = 650
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING_BOX)
        wall.center_x = 800
        wall.center_y = 600
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING_BOX)
        wall.center_x = 500
        wall.center_y = 800
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING_BOX)
        wall.center_x = 450
        wall.center_y = 750
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING_BOX)
        wall.center_x = 550
        wall.center_y = 750
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING_BOX)
        wall.center_x = 800
        wall.center_y = 850
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING_BOX)
        wall.center_x = 900
        wall.center_y = 850
        self.wall_list.append(wall)

        wall = arcade.Sprite("tileYellow_02.png", SPRITE_SCALING_BOX)
        wall.center_x = 850
        wall.center_y = 800
        self.wall_list.append(wall)

    def on_draw(self):
        arcade.start_render()

        self.camera_for_sprites.use()

        self.wall_list.draw()
        self.player_list.draw()

        self.camera_for_gui.use()
        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.WHITE, 24)

    def on_update(self, delta_time):
        """ Movement and game logic """

        self.physics_engine.update()

        lower_left_corner = (self.player_sprite.center_x - self.width / 2,
                             self.player_sprite.center_y - self.height / 2)
        self.camera_for_sprites.move_to(lower_left_corner, CAMERA_SPEED)

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
