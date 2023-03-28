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
    def __init__(self, width, height, title):

