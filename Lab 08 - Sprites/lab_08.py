
import random
import arcade

SPRITE_SCALING = 0.25
STAR_COUNT = 50

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 8")

        self.player_list = None
        self.star_list = None

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.EERIE_BLACK)

    def setup(self):

        self.player_list = arcade.SpriteList()
        self.star_list = arcade.SpriteList()

        self.score = 0

        self.player_sprite = arcade.Sprite("alienBlue_front.png", SPRITE_SCALING)
        self.player_sprite.center_x = 350
        self.player_sprite.center_y = 350
        self.player_list.append(self.player_sprite)

        for i in range(STAR_COUNT):

            # Blob image from kenney.nl
            star = arcade.Sprite("star.png", SPRITE_SCALING)

            star.center_x = random.randrange(SCREEN_WIDTH)
            star.center_y = random.randrange(SCREEN_HEIGHT)

            self.star_list.append(star)

    def on_draw(self):
        arcade.start_render()

        self.star_list.draw()
        self.player_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):

        self.star_list.update()

        star_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.star_list)

        for star in star_hit_list:
            star.remove_from_sprite_lists()
            self.score += 1


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
