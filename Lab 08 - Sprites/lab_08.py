import random
import arcade
import math

SPRITE_SCALING = 0.25
BLOB_COUNT = 100

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700


class MyGame(arcade.Window):

    def __init__(self):
        super.__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 8")
