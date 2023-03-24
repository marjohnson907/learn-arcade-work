
import random
import arcade
import math

SPRITE_SCALING = 0.25
STAR_COUNT = 25
FIREBALL_COUNT = 5

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
PLAYER_MOVEMENT_SPEED = 3
SPRITE_SPEED = 0.5


class Star(arcade.Sprite):

    def reset_pos(self):
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        self.center_y -= 1

        if self.top < 0:
            self.reset_pos()


class Fireball(arcade.Sprite):

    def follow_sprite(self, player_sprite):

        if self.center_y < player_sprite.center_y:
            self.center_y += min(SPRITE_SPEED, player_sprite.center_y - self.center_y)
        elif self.center_y > player_sprite.center_y:
            self.center_y -= min(SPRITE_SPEED, self.center_y - player_sprite.center_y)

        if self.center_x < player_sprite.center_x:
            self.center_x += min(SPRITE_SPEED, player_sprite.center_x - self.center_x)
        elif self.center_x > player_sprite.center_x:
            self.center_x -= min(SPRITE_SPEED, self.center_x - player_sprite.center_x)


class Player(arcade.Sprite):

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Check for out-of-bounds
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 8")

        self.player_list = None
        self.star_list = None
        self.fireball_list = None

        self.player_sprite = None
        self.score = 0

        arcade.set_background_color(arcade.color.EERIE_BLACK)

    def setup(self):

        self.player_list = arcade.SpriteList()
        self.star_list = arcade.SpriteList()
        self.fireball_list = arcade.SpriteList()

        self.score = 0

        self.player_sprite = Player("alienBlue_front.png", SPRITE_SCALING)
        self.player_sprite.center_x = 350
        self.player_sprite.center_y = 350
        self.player_list.append(self.player_sprite)

        for i in range(STAR_COUNT):

            # Star image from kenney.nl
            star = Star("star.png", SPRITE_SCALING)

            star.center_x = random.randrange(SCREEN_WIDTH)
            star.center_y = random.randrange(SCREEN_HEIGHT)

            self.star_list.append(star)

        for i in range(FIREBALL_COUNT):

            # Fireball image from kenney.nl
            fireball = Fireball("fireball.png", SPRITE_SCALING)

            fireball.center_x = random.randrange(SCREEN_WIDTH)
            fireball.center_y = random.randrange(SCREEN_HEIGHT)

            self.fireball_list.append(fireball)

    def on_draw(self):
        arcade.start_render()

        self.star_list.draw()
        self.fireball_list.draw()
        self.player_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def update(self, delta_time):

        self.player_list.update()

        self.star_list.update()

        star_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.star_list)

        for star in star_hit_list:
            star.remove_from_sprite_lists()
            self.score += 1

        self.fireball_list.update()

        fireball_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.fireball_list)

        for fireball in fireball_hit_list:
            fireball.remove_from_sprite_lists()
            self.score -= 1


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
