import arcade
import random
import math


SPRITE_SCALING = 0.5
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
NUMBER_OF_COINS = 1
NUMBER_OF_STARS = 1
MOVEMENT_SPEED = 5
ENEMY_SPEED = 1
ENEMY_NUMBER = 1


class Enemy(arcade.Sprite):
    """Enemy class"""

    def follow_sprite(self, player_sprite):
        """
        This function will move the current sprite towards whatever
        other sprite is specified as a parameter.

        We use the 'min' function here to get the sprite to line up with
        the target sprite, and not jump around if the sprite is not off
        an exact multiple of SPRITE_SPEED.
        """

        self.center_x += self.change_x
        self.center_y += self.change_y

        # Random 1 in 100 chance that we'll change from our old direction and
        # then re-aim toward the player
        if random.randrange(100) == 0:
            start_x = self.center_x
            start_y = self.center_y

            # Get the destination location for the bullet
            dest_x = player_sprite.center_x
            dest_y = player_sprite.center_y

            # Do math to calculate how to get the bullet to the destination.
            # Calculation the angle in radians between the start points
            # and end points. This is the angle the bullet will travel.
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            # Taking into account the angle, calculate our change_x
            # and change_y. Velocity is how fast the bullet travels.
            self.change_x = math.cos(angle) * ENEMY_SPEED
            self.change_y = math.sin(angle) * ENEMY_SPEED


class Room:
    """Room class"""
    def __init__(self):
        # Lists
        self.wall_list = None
        self.coin_list = None
        self.star_list = None
        self.enemy_list = None


def setup_room_1():
    """Room 1"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.coin_list = arcade.SpriteList()
    room.star_list = arcade.SpriteList()
    room.enemy_list = arcade.SpriteList()

    # Walls, Room 1, image from https://kenney.nl
    for y in (0, SCREEN_HEIGHT - 16):
        for x in range(0, SCREEN_WIDTH, 32):
            wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    for y in range(0, 200, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = 0
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(300, SCREEN_HEIGHT, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = 0
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(100, 200, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = 100
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(400, 600, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = 100
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(200, 500, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = 200
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(300, 500, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = 300
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(300, 400, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = 400
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(500, 600, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = 400
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(200, 300, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = 500
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(400, 500, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = 500
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(100, 200, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = 600
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(500, 600, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = 600
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(400, 500, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = 700
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(100, 200, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = 800
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(300, 500, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = 800
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(200, 300, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = 900
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(400, 600, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = 900
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(0, 200, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = 1000
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(100, 200, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = 1100
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(0, 300, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = SCREEN_WIDTH
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(400, SCREEN_HEIGHT, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = SCREEN_WIDTH
        wall.center_y = y
        room.wall_list.append(wall)

    for x in range(100, 500, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 100
        room.wall_list.append(wall)

    for x in range(600, 800, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 100
        room.wall_list.append(wall)

    for x in range(900, 1000, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 100
        room.wall_list.append(wall)

    for x in range(0, 100, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 200
        room.wall_list.append(wall)

    for x in range(200, 600, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 200
        room.wall_list.append(wall)

    for x in range(700, 900, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 200
        room.wall_list.append(wall)

    for x in range(1100, 1200, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 200
        room.wall_list.append(wall)

    for x in range(0, 200, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 300
        room.wall_list.append(wall)

    for x in range(600, 800, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 300
        room.wall_list.append(wall)

    for x in range(900, 1100, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 300
        room.wall_list.append(wall)

    for x in range(300, 400, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 400
        room.wall_list.append(wall)

    for x in range(500, 700, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 400
        room.wall_list.append(wall)

    for x in range(800, 1100, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 400
        room.wall_list.append(wall)

    for x in range(200, 300, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 500
        room.wall_list.append(wall)

    for x in range(400, 500, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 500
        room.wall_list.append(wall)

    for x in range(1000, 1200, 32):
        wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 500
        room.wall_list.append(wall)

    # Coins, image from https://kenney.nl
    for i in range(NUMBER_OF_COINS):
        coin = arcade.Sprite("coinGold.png", SPRITE_SCALING/2)

        # Boolean variable coin placement
        coin_placed_successfully = False

        while not coin_placed_successfully:
            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH - 25)
            coin.center_y = random.randrange(SCREEN_HEIGHT - 25)

            # See if the coin is hitting a wall
            wall_hit_list = arcade.check_for_collision_with_list(coin, room.wall_list)
            # See if the coin is hitting another coin
            coin_hit_list = arcade.check_for_collision_with_list(coin, room.coin_list)
            if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                # It is!
                coin_placed_successfully = True
        # Add the coin to the lists
        room.coin_list.append(coin)

    # Zombie, image from https://kenney.nl
    """for i in range(ENEMY_NUMBER):
        position_list = [[1150, 450],
                         [1150, 350],
                         [1150, 250]]
        enemy = Enemy("character_zombie_hit.png", SPRITE_SCALING, position_list)
        # Position the zombie
        enemy.center_x = position_list[0][0]
        enemy.center_y = position_list[0][1]
        # Add the zombie to the lists
        room.enemy_list.append(enemy)"""

    return room


def setup_room_2():
    """Room 2"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.coin_list = arcade.SpriteList()
    room.star_list = arcade.SpriteList()
    room.enemy_list = arcade.SpriteList()

    # Walls, Room 2, image from https://kenney.nl
    for y in (0, SCREEN_HEIGHT - 16):
        for x in range(0, SCREEN_WIDTH, 32):
            wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    for y in range(0, 300, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = 0
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(400, SCREEN_HEIGHT, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = 0
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(300, 400, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = 100
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(100, 200, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = 200
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(500, 600, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = 200
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(100, 300, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = 300
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(400, 500, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = 300
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(100, 400, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = 400
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(500, 600, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = 400
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(0, 100, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = 500
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(300, 500, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = 500
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(200, 300, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = 600
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(400, 600, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = 600
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(100, 300, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = 700
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(400, 600, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = 700
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(0, 100, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = 800
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(100, 300, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = 900
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(400, 500, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = 900
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(0, 100, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = 1000
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(300, 500, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = 1000
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(100, 300, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = 1100
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(500, 600, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = 1100
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(0, 200, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = SCREEN_WIDTH
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(300, SCREEN_HEIGHT, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = SCREEN_WIDTH
        wall.center_y = y
        room.wall_list.append(wall)

    for x in range(100, 200, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 100
        room.wall_list.append(wall)

    for x in range(300, 400, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 100
        room.wall_list.append(wall)

    for x in range(500, 600, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 100
        room.wall_list.append(wall)

    for x in range(700, 800, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 100
        room.wall_list.append(wall)

    for x in range(0, 200, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 200
        room.wall_list.append(wall)

    for x in range(500, 700, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 200
        room.wall_list.append(wall)

    for x in range(800, 1200, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 200
        room.wall_list.append(wall)

    for x in range(100, 300, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 300
        room.wall_list.append(wall)

    for x in range(400, 500, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 300
        room.wall_list.append(wall)

    for x in range(700, 800, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 300
        room.wall_list.append(wall)

    for x in range(100, 300, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 400
        room.wall_list.append(wall)

    for x in range(700, 800, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 400
        room.wall_list.append(wall)

    for x in range(900, 1200, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 400
        room.wall_list.append(wall)

    for x in range(0, 100, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 500
        room.wall_list.append(wall)

    for x in range(800, 900, 32):
        wall = arcade.Sprite("tileBlue_03.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 500
        room.wall_list.append(wall)

    # Coins, image from https://kenney.nl
    for i in range(NUMBER_OF_COINS):
        coin = arcade.Sprite("coinSilver.png", SPRITE_SCALING/2)

        # Boolean variable coin placement
        coin_placed_successfully = False

        while not coin_placed_successfully:
            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH - 25)
            coin.center_y = random.randrange(SCREEN_HEIGHT - 25)

            # See if the coin is hitting a wall
            wall_hit_list = arcade.check_for_collision_with_list(coin, room.wall_list)
            # See if the coin is hitting another coin
            coin_hit_list = arcade.check_for_collision_with_list(coin, room.coin_list)
            if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                # It is!
                coin_placed_successfully = True
        # Add the coin to the lists
        room.coin_list.append(coin)

    # Stars, image from https://kenney.nl
    for i in range(NUMBER_OF_STARS):
        star = arcade.Sprite("star.png", SPRITE_SCALING/2)

        # Boolean variable star placement
        star_placed_successfully = False

        while not star_placed_successfully:
            # Position the stars
            star.center_x = random.randrange(SCREEN_WIDTH - 25)
            star.center_y = random.randrange(SCREEN_HEIGHT - 25)

            # See if the star is hitting a wall
            wall_hit_list = arcade.check_for_collision_with_list(star, room.wall_list)
            # See if the star is hitting another star or coin
            star_hit_list = arcade.check_for_collision_with_list(coin, room.coin_list, room.star_list)
            if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                # It is!
                star_placed_successfully = True
        # Add the star to the lists
        room.star_list.append(star)

    # Alien, image from https://kenney.nl
    """for i in range(ENEMY_NUMBER):
        position_list = [[1150, 500],
                         [1150, 50]]
        enemy = Enemy("alienBlue_front.png", SPRITE_SCALING, position_list)
        # Position the alien
        enemy.center_x = position_list[0][0]
        enemy.center_y = position_list[0][1]
        # Add the alien to the lists
        room.enemy_list.append(enemy)"""

    return room


def setup_room_3():
    """Room 3"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.coin_list = arcade.SpriteList()
    room.star_list = arcade.SpriteList()
    room.enemy_list = arcade.SpriteList()

    # Walls, Room 3, image from https://kenney.nl
    for y in (0, SCREEN_HEIGHT - 16):
        for x in range(0, SCREEN_WIDTH, 32):
            wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    for y in range(0, 200, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = 0
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(300, SCREEN_HEIGHT, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = 0
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(200, 500, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = 100
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(100, 200, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = 200
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(500, 600, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = 200
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(0, 100, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = 300
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(100, 500, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = 400
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(100, 200, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = 500
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(200, 500, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = 600
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(100, 200, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = 700
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(300, 400, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = 700
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(500, 600, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = 700
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(0, 100, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = 800
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(200, 500, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = 800
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(100, 200, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = 900
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(400, 600, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = 900
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(0, 100, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = 1000
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(300, 400, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = 1000
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(400, 500, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = 1100
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(0, 300, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = SCREEN_WIDTH
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(400, SCREEN_HEIGHT, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = SCREEN_WIDTH
        wall.center_y = y
        room.wall_list.append(wall)

    for x in range(100, 200, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 100
        room.wall_list.append(wall)

    for x in range(300, 400, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 100
        room.wall_list.append(wall)

    for x in range(500, 700, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 100
        room.wall_list.append(wall)

    for x in range(800, 900, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 100
        room.wall_list.append(wall)

    for x in range(1000, 1100, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 100
        room.wall_list.append(wall)

    for x in range(100, 300, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 200
        room.wall_list.append(wall)

    for x in range(700, 800, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 200
        room.wall_list.append(wall)

    for x in range(900, 1100, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 200
        room.wall_list.append(wall)

    for x in range(0, 100, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 300
        room.wall_list.append(wall)

    for x in range(200, 400, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 300
        room.wall_list.append(wall)

    for x in range(500, 600, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 300
        room.wall_list.append(wall)

    for x in range(800, 1200, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 300
        room.wall_list.append(wall)

    for x in range(100, 300, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 400
        room.wall_list.append(wall)

    for x in range(400, 500, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 400
        room.wall_list.append(wall)

    for x in range(600, 700, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 400
        room.wall_list.append(wall)

    for x in range(200, 300, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 500
        room.wall_list.append(wall)

    for x in range(400, 600, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 500
        room.wall_list.append(wall)

    for x in range(900, 1100, 32):
        wall = arcade.Sprite("ground_05.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 500
        room.wall_list.append(wall)

    # Flowers, image from https://kenney.nl
    for i in range(NUMBER_OF_COINS):
        coin = arcade.Sprite("foliagePack_001.png", SPRITE_SCALING)

        # Boolean variable coin placement
        coin_placed_successfully = False

        while not coin_placed_successfully:
            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH - 25)
            coin.center_y = random.randrange(SCREEN_HEIGHT - 25)

            # See if the coin is hitting a wall
            wall_hit_list = arcade.check_for_collision_with_list(coin, room.wall_list)
            # See if the coin is hitting another coin
            coin_hit_list = arcade.check_for_collision_with_list(coin, room.coin_list)
            if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                # It is!
                coin_placed_successfully = True
        # Add the coin to the lists
        room.coin_list.append(coin)

    # Mushroom, image from https://kenney.nl
    for i in range(NUMBER_OF_STARS):
        star = arcade.Sprite("mushroomRed.png", SPRITE_SCALING/2)

        # Boolean variable star placement
        star_placed_successfully = False

        while not star_placed_successfully:
            # Position the stars
            star.center_x = random.randrange(SCREEN_WIDTH - 25)
            star.center_y = random.randrange(SCREEN_HEIGHT - 25)

            # See if the star is hitting a wall
            wall_hit_list = arcade.check_for_collision_with_list(star, room.wall_list)
            # See if the star is hitting another star or coin
            star_hit_list = arcade.check_for_collision_with_list(coin, room.coin_list, room.star_list)
            if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                # It is!
                star_placed_successfully = True
        # Add the star to the lists
        room.star_list.append(star)

    # Bee, image from https://kenney.nl
    """for i in range(ENEMY_NUMBER):
        position_list = [[1150, 500],
                         [1150, 50]]
        enemy = Enemy("bee.png", SPRITE_SCALING, position_list)
        # Position the bee
        enemy.center_x = position_list[0][0]
        enemy.center_y = position_list[0][1]
        # Add the bee to the lists
        room.enemy_list.append(enemy)"""

    return room


def setup_room_4():
    """Room 4"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.coin_list = arcade.SpriteList()
    room.star_list = arcade.SpriteList()
    room.enemy_list = arcade.SpriteList()

    # Walls, Room 4, image from https://kenney.nl
    for x in range(50, SCREEN_WIDTH, 63):
        wall = arcade.Sprite("waterTop_high.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 0
        room.wall_list.append(wall)

    for x in range(0, SCREEN_WIDTH, 63):
        wall = arcade.Sprite("waterTop_high.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = SCREEN_HEIGHT
        room.wall_list.append(wall)

    for y in range(0, 300, 32):
        wall = arcade.Sprite("water.png", SPRITE_SCALING/2)
        wall.center_x = 0
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(400, SCREEN_HEIGHT, 32):
        wall = arcade.Sprite("water.png", SPRITE_SCALING/2)
        wall.center_x = 0
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(0, 100, 32):
        wall = arcade.Sprite("water.png", SPRITE_SCALING/2)
        wall.center_x = 100
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(200, 400, 32):
        wall = arcade.Sprite("water.png", SPRITE_SCALING/2)
        wall.center_x = 100
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(100, 200, 32):
        wall = arcade.Sprite("water.png", SPRITE_SCALING/2)
        wall.center_x = 200
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(0, 100, 32):
        wall = arcade.Sprite("water.png", SPRITE_SCALING/2)
        wall.center_x = 300
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(300, 600, 32):
        wall = arcade.Sprite("water.png", SPRITE_SCALING/2)
        wall.center_x = 300
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(100, 300, 32):
        wall = arcade.Sprite("water.png", SPRITE_SCALING/2)
        wall.center_x = 400
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(200, 500, 32):
        wall = arcade.Sprite("water.png", SPRITE_SCALING/2)
        wall.center_x = 500
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(100, 200, 32):
        wall = arcade.Sprite("water.png", SPRITE_SCALING/2)
        wall.center_x = 600
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(400, 600, 32):
        wall = arcade.Sprite("water.png", SPRITE_SCALING/2)
        wall.center_x = 600
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(0, 200, 32):
        wall = arcade.Sprite("water.png", SPRITE_SCALING/2)
        wall.center_x = 700
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(300, 500, 32):
        wall = arcade.Sprite("water.png", SPRITE_SCALING/2)
        wall.center_x = 700
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(100, 200, 32):
        wall = arcade.Sprite("water.png", SPRITE_SCALING/2)
        wall.center_x = 800
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(500, 600, 32):
        wall = arcade.Sprite("water.png", SPRITE_SCALING/2)
        wall.center_x = 800
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(100, 400, 32):
        wall = arcade.Sprite("water.png", SPRITE_SCALING/2)
        wall.center_x = 900
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(100, 300, 32):
        wall = arcade.Sprite("water.png", SPRITE_SCALING/2)
        wall.center_x = 1000
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(200, 300, 32):
        wall = arcade.Sprite("water.png", SPRITE_SCALING/2)
        wall.center_x = 1100
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(0, 200, 32):
        wall = arcade.Sprite("water.png", SPRITE_SCALING/2)
        wall.center_x = SCREEN_WIDTH
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(300, SCREEN_HEIGHT, 32):
        wall = arcade.Sprite("water.png", SPRITE_SCALING/2)
        wall.center_x = SCREEN_WIDTH
        wall.center_y = y
        room.wall_list.append(wall)

    for x in range(400, 600, 32):
        wall = arcade.Sprite("water.png", SPRITE_SCALING/2)
        wall.center_x = x
        wall.center_y = 100
        room.wall_list.append(wall)

    for x in range(800, 900, 32):
        wall = arcade.Sprite("water.png", SPRITE_SCALING/2)
        wall.center_x = x
        wall.center_y = 100
        room.wall_list.append(wall)

    for x in range(1000, 1100, 32):
        wall = arcade.Sprite("water.png", SPRITE_SCALING/2)
        wall.center_x = x
        wall.center_y = 100
        room.wall_list.append(wall)

    for x in range(100, 300, 32):
        wall = arcade.Sprite("water.png", SPRITE_SCALING/2)
        wall.center_x = x
        wall.center_y = 200
        room.wall_list.append(wall)

    for x in range(600, 700, 32):
        wall = arcade.Sprite("water.png", SPRITE_SCALING/2)
        wall.center_x = x
        wall.center_y = 200
        room.wall_list.append(wall)

    for x in range(1100, 1200, 32):
        wall = arcade.Sprite("water.png", SPRITE_SCALING/2)
        wall.center_x = x
        wall.center_y = 200
        room.wall_list.append(wall)

    for x in range(200, 300, 32):
        wall = arcade.Sprite("water.png", SPRITE_SCALING/2)
        wall.center_x = x
        wall.center_y = 300
        room.wall_list.append(wall)

    for x in range(500, 900, 32):
        wall = arcade.Sprite("water.png", SPRITE_SCALING/2)
        wall.center_x = x
        wall.center_y = 300
        room.wall_list.append(wall)

    for x in range(1000, 1100, 32):
        wall = arcade.Sprite("water.png", SPRITE_SCALING/2)
        wall.center_x = x
        wall.center_y = 300
        room.wall_list.append(wall)

    for x in range(100, 300, 32):
        wall = arcade.Sprite("water.png", SPRITE_SCALING/2)
        wall.center_x = x
        wall.center_y = 400
        room.wall_list.append(wall)

    for x in range(400, 500, 32):
        wall = arcade.Sprite("water.png", SPRITE_SCALING/2)
        wall.center_x = x
        wall.center_y = 400
        room.wall_list.append(wall)

    for x in range(700, 800, 32):
        wall = arcade.Sprite("water.png", SPRITE_SCALING/2)
        wall.center_x = x
        wall.center_y = 400
        room.wall_list.append(wall)

    for x in range(900, 1200, 32):
        wall = arcade.Sprite("water.png", SPRITE_SCALING/2)
        wall.center_x = x
        wall.center_y = 400
        room.wall_list.append(wall)

    for x in range(0, 200, 32):
        wall = arcade.Sprite("water.png", SPRITE_SCALING/2)
        wall.center_x = x
        wall.center_y = 500
        room.wall_list.append(wall)

    for x in range(300, 400, 32):
        wall = arcade.Sprite("water.png", SPRITE_SCALING/2)
        wall.center_x = x
        wall.center_y = 500
        room.wall_list.append(wall)

    for x in range(800, 1100, 32):
        wall = arcade.Sprite("water.png", SPRITE_SCALING/2)
        wall.center_x = x
        wall.center_y = 500
        room.wall_list.append(wall)

    # Red fish, image from https://kenney.nl
    for i in range(NUMBER_OF_COINS):
        coin = arcade.Sprite("fishTile_078.png", SPRITE_SCALING)

        # Boolean variable fish placement
        coin_placed_successfully = False

        while not coin_placed_successfully:
            # Position the fish
            coin.center_x = random.randrange(SCREEN_WIDTH - 25)
            coin.center_y = random.randrange(SCREEN_HEIGHT - 25)

            # See if the fish is hitting a wall
            wall_hit_list = arcade.check_for_collision_with_list(coin, room.wall_list)
            # See if the fish is hitting another coin
            coin_hit_list = arcade.check_for_collision_with_list(coin, room.coin_list)
            if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                # It is!
                coin_placed_successfully = True
        # Add the fish to the lists
        room.coin_list.append(coin)

    # Puffer fish, image from https://kenney.nl
    for i in range(NUMBER_OF_STARS):
        star = arcade.Sprite("fishTile_100.png", SPRITE_SCALING)

        # Boolean variable puffer fish placement
        star_placed_successfully = False

        while not star_placed_successfully:
            # Position the puffer fish
            star.center_x = random.randrange(SCREEN_WIDTH - 25)
            star.center_y = random.randrange(SCREEN_HEIGHT - 25)

            # See if the puffer fish is hitting a wall
            wall_hit_list = arcade.check_for_collision_with_list(star, room.wall_list)
            # See if the puffer fish is hitting another fish
            star_hit_list = arcade.check_for_collision_with_list(coin, room.coin_list, room.star_list)
            if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                # It is!
                star_placed_successfully = True
        # Add the puffer fish to the lists
        room.star_list.append(star)

    # Enemy fish, image from https://kenney.nl
    """for i in range(ENEMY_NUMBER):
        position_list = [[1150, 500],
                         [1150, 50]]
        enemy = Enemy("fishTile_090.png", SPRITE_SCALING, position_list)
        # Position the enemy fish
        enemy.center_x = position_list[0][0]
        enemy.center_y = position_list[0][1]
        # Add the enemy fish to the lists
        room.enemy_list.append(enemy)"""

    return room


def setup_room_5():
    """Room 5"""
    room = Room()

    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.coin_list = arcade.SpriteList()
    room.star_list = arcade.SpriteList()
    room.enemy_list = arcade.SpriteList()

    # Walls, Room 5, image from https://kenney.nl
    for x in range(50, SCREEN_WIDTH, 63):
        wall = arcade.Sprite("lavaTop_high.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 0
        room.wall_list.append(wall)

    for x in range(0, SCREEN_WIDTH, 63):
        wall = arcade.Sprite("lavaTop_high.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = SCREEN_HEIGHT
        room.wall_list.append(wall)

    for y in range(0, 200, 32):
        wall = arcade.Sprite("lava.png", SPRITE_SCALING/2)
        wall.center_x = 0
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(300, SCREEN_HEIGHT, 32):
        wall = arcade.Sprite("lava.png", SPRITE_SCALING/2)
        wall.center_x = 0
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(0, 100, 32):
        wall = arcade.Sprite("lava.png", SPRITE_SCALING/2)
        wall.center_x = 100
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(300, 500, 32):
        wall = arcade.Sprite("lava.png", SPRITE_SCALING/2)
        wall.center_x = 100
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(100, 300, 32):
        wall = arcade.Sprite("lava.png", SPRITE_SCALING/2)
        wall.center_x = 200
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(500, 600, 32):
        wall = arcade.Sprite("lava.png", SPRITE_SCALING)
        wall.center_x = 200
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(0, 300, 32):
        wall = arcade.Sprite("lava.png", SPRITE_SCALING)
        wall.center_x = 300
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(400, 500, 32):
        wall = arcade.Sprite("lava.png", SPRITE_SCALING)
        wall.center_x = 300
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(0, 300, 32):
        wall = arcade.Sprite("lava.png", SPRITE_SCALING)
        wall.center_x = SCREEN_WIDTH
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(400, SCREEN_HEIGHT, 32):
        wall = arcade.Sprite("lava.png", SPRITE_SCALING)
        wall.center_x = SCREEN_WIDTH
        wall.center_y = y
        room.wall_list.append(wall)

    # Coin, image from https://kenney.nl
    for i in range(NUMBER_OF_COINS):
        coin = arcade.Sprite("coinGold.png", SPRITE_SCALING/2)

        # Boolean variable coin placement
        coin_placed_successfully = False

        while not coin_placed_successfully:
            # Position the coins
            coin.center_x = random.randrange(SCREEN_WIDTH - 25)
            coin.center_y = random.randrange(SCREEN_HEIGHT - 25)

            # See if the coin is hitting a wall
            wall_hit_list = arcade.check_for_collision_with_list(coin, room.wall_list)
            # See if the coin is hitting another coin
            coin_hit_list = arcade.check_for_collision_with_list(coin, room.coin_list)
            if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                # It is!
                coin_placed_successfully = True
        # Add the coin to the lists
        room.coin_list.append(coin)

    # Stars, image from https://kenney.nl
    for i in range(NUMBER_OF_STARS):
        star = arcade.Sprite("star.png", SPRITE_SCALING/2)

        # Boolean variable star placement
        star_placed_successfully = False

        while not star_placed_successfully:
            # Position the stars
            star.center_x = random.randrange(SCREEN_WIDTH - 25)
            star.center_y = random.randrange(SCREEN_HEIGHT - 25)

            # See if the star is hitting a wall
            wall_hit_list = arcade.check_for_collision_with_list(star, room.wall_list)
            # See if the star is hitting another star or coin
            star_hit_list = arcade.check_for_collision_with_list(coin, room.coin_list, room.star_list)
            if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                # It is!
                star_placed_successfully = True
        # Add the star to the lists
        room.star_list.append(star)

    # Bomb, image from https://kenney.nl
    """for i in range(ENEMY_NUMBER):
        position_list = [[1150, 500],
                         [1150, 50]]
        enemy = Enemy("bomb.png", SPRITE_SCALING, position_list)
        # Position the bomb
        enemy.center_x = position_list[0][0]
        enemy.center_y = position_list[0][1]
        # Add the bomb to the lists
        room.enemy_list.append(enemy)"""

    return room


class GameView(arcade.View):
    """ Main application class. """

    def __init__(self):
        """Initializer"""
        super().__init__()

        # Sprite lists
        self.current_room = 0

        # Set up the player
        self.rooms = None
        self.player_sprite = None
        self.enemy = None
        self.player_list = None
        self.coin_list = None
        self.star_list = None
        self.enemy_list = None
        self.physics_engine = None
        self.enemy_physics_engine = None
        # Sound
        self.laser_sound = arcade.load_sound("laser.wav")

    def setup(self):
        """ Set up the game and initialize the variables. """
        # Set up the player
        self.player_sprite = arcade.Sprite("player_05.png", SPRITE_SCALING)
        self.player_sprite.center_x = 0
        self.player_sprite.center_y = 250
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)
        # Set up enemy

        self.enemy = Enemy("character_zombie_hit.png", SPRITE_SCALING)

        # Position the coin
        self.enemy.center_x = 1150
        self.enemy.center_y = 550


            # Add the coin to the lists

        self.enemy_list = arcade.SpriteList()
        self.enemy_list.append(self.enemy)
        self.coin_list = arcade.SpriteList()
        self.star_list = arcade.SpriteList()

        # Our list of rooms
        self.rooms = []

        # Create the rooms. Extend the pattern for each room.
        room = setup_room_1()
        self.rooms.append(room)

        room = setup_room_2()
        self.rooms.append(room)

        room = setup_room_3()
        self.rooms.append(room)

        room = setup_room_4()
        self.rooms.append(room)

        room = setup_room_5()
        self.rooms.append(room)

        # Our starting room number
        self.current_room = 0

        # Create a physics engine for this room
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)

        # Reset the score
        self.score = 0

    def on_draw(self):
        """Render the screen."""
        self.clear()

        # Draw walls
        self.rooms[self.current_room].wall_list.draw()

        # Draw coins
        self.rooms[self.current_room].coin_list.draw()

        # Draw stars
        self.rooms[self.current_room].star_list.draw()

        # Draw enemy
        self.enemy_list.draw()

        # Draw player
        self.player_list.draw()

        # Score
        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.WHITE, 24)

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

    def on_update(self, delta_time):
        """ Movement and game logic """

        self.physics_engine.update()
        self.coin_list.update()
        self.star_list.update()
        self.enemy_list.update()


        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.rooms[self.current_room].coin_list)
        star_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.rooms[self.current_room].star_list)
        enemy_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.rooms[self.current_room].enemy_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            arcade.play_sound(self.laser_sound)
            coin.remove_from_sprite_lists()
            self.score += 1
        for star in star_hit_list:
            arcade.play_sound(self.laser_sound)
            star.remove_from_sprite_lists()
            self.score += 5
        for enemy in enemy_hit_list:
            arcade.play_sound(self.laser_sound)
            self.score -= 1

        # If score drops below 0, game ends
        if self.score < 0:
            view = GameOverView()
            self.window.show_view(view)

        # Room logic
        if self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 0:
            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 0
        if self.player_sprite.center_x < 0 and self.current_room == 1:
            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = SCREEN_WIDTH
        if self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 1:
            self.current_room = 2
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 0
        if self.player_sprite.center_x < 0 and self.current_room == 1:
            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = SCREEN_WIDTH
        if self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 2:
            self.current_room = 3
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 0
        if self.player_sprite.center_x < 0 and self.current_room == 2:
            self.current_room = 2
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = SCREEN_WIDTH
        if self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 3:
            self.current_room = 4
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 0
        if self.player_sprite.center_x < 0 and self.current_room == 3:
            self.current_room = 3
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = SCREEN_WIDTH
        if self.player_sprite.center_x < 0 and self.current_room == 4:
            self.current_room = 4
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = SCREEN_WIDTH
        elif self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 4:
            view = GameOverView()
            self.window.show_view(view)


class GameOverView(arcade.View):
    """Game Over Screen"""
    def __init__(self):
        super().__init__()

    def on_show_view(self):
        arcade.set_background_color(arcade.color.CORAL_RED)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Game Over", 250, SCREEN_HEIGHT/2, arcade.color.DARK_SIENNA, 100)


def main():
    """ Main function """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT)
    start_view = GameView()
    window.show_view(start_view)
    start_view.setup()
    arcade.run()


if __name__ == "__main__":
    main()
