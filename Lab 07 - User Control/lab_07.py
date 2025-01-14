""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3


def draw_sunset():
    arcade.draw_rectangle_filled(400, 450, 800, 100, arcade.color.BRIGHT_PINK)
    arcade.draw_rectangle_filled(400, 350, 800, 100, arcade.color.WILD_STRAWBERRY)
    arcade.draw_rectangle_filled(400, 250, 800, 100, arcade.color.WILD_WATERMELON)


def draw_mountains():
    # Mountains
    arcade.draw_triangle_filled(175, 100, 575, 100, 375, 450, arcade.color.ROYAL_PURPLE)
    arcade.draw_triangle_filled(400, 100, 800, 100, 600, 500, arcade.color.ROYAL_PURPLE)
    arcade.draw_triangle_filled(0, 0, 500, 0, 250, 350, arcade.color.REGALIA)
    arcade.draw_triangle_filled(200, 0, 750, 0, 475, 450, arcade.color.REGALIA)
    arcade.draw_polygon_filled(((0, 0),
                               (0, 200),
                               (100, 325),
                               (425, 0)),
                               arcade.color.REGALIA)
    arcade.draw_polygon_filled(((800, 0),
                               (800, 250),
                               (700, 400),
                               (400, 0)),
                               arcade.color.REGALIA)


def draw_background_trees():
    # Back trees
    arcade.draw_polygon_filled(((0, 0),
                               (0, 50),
                               (50, 150),
                               (100, 50)),
                               arcade.color.OLD_BURGUNDY)
    arcade.draw_triangle_filled(5, 110, 95, 110, 50, 200, arcade.color.OLD_BURGUNDY)

    arcade.draw_triangle_filled(95, 0, 155, 0, 125, 190, arcade.color.TAUPE)
    arcade.draw_triangle_filled(95, 80, 155, 80, 125, 190, arcade.color.TAUPE)
    arcade.draw_triangle_filled(100, 150, 150, 150, 125, 190, arcade.color.TAUPE)

    arcade.draw_triangle_filled(170, 0, 230, 0, 200, 210, arcade.color.OLD_BURGUNDY)
    arcade.draw_triangle_filled(170, 80, 230, 80, 200, 210, arcade.color.OLD_BURGUNDY)
    arcade.draw_triangle_filled(175, 150, 225, 150, 200, 210, arcade.color.OLD_BURGUNDY)

    arcade.draw_triangle_filled(270, 0, 330, 0, 300, 190, arcade.color.OLD_BURGUNDY)
    arcade.draw_triangle_filled(270, 80, 330, 80, 300, 190, arcade.color.OLD_BURGUNDY)
    arcade.draw_triangle_filled(275, 150, 325, 150, 300, 190, arcade.color.OLD_BURGUNDY)

    arcade.draw_triangle_filled(370, 0, 430, 0, 400, 200, arcade.color.OLD_BURGUNDY)
    arcade.draw_triangle_filled(370, 80, 430, 80, 400, 200, arcade.color.OLD_BURGUNDY)
    arcade.draw_triangle_filled(375, 150, 425, 150, 400, 200, arcade.color.OLD_BURGUNDY)

    arcade.draw_triangle_filled(445, 0, 505, 0, 475, 190, arcade.color.TAUPE)
    arcade.draw_triangle_filled(445, 80, 505, 80, 475, 190, arcade.color.TAUPE)
    arcade.draw_triangle_filled(450, 150, 500, 150, 475, 190, arcade.color.TAUPE)

    arcade.draw_triangle_filled(470, 0, 530, 0, 500, 210, arcade.color.OLD_BURGUNDY)
    arcade.draw_triangle_filled(470, 80, 530, 80, 500, 210, arcade.color.OLD_BURGUNDY)
    arcade.draw_triangle_filled(475, 150, 525, 150, 500, 210, arcade.color.OLD_BURGUNDY)

    arcade.draw_triangle_filled(535, 0, 605, 0, 575, 190, arcade.color.TAUPE)
    arcade.draw_triangle_filled(535, 80, 605, 80, 575, 190, arcade.color.TAUPE)
    arcade.draw_triangle_filled(540, 150, 600, 150, 575, 190, arcade.color.TAUPE)

    arcade.draw_triangle_filled(570, 0, 630, 0, 600, 210, arcade.color.OLD_BURGUNDY)
    arcade.draw_triangle_filled(570, 80, 630, 80, 600, 210, arcade.color.OLD_BURGUNDY)
    arcade.draw_triangle_filled(575, 150, 625, 150, 600, 210, arcade.color.OLD_BURGUNDY)

    arcade.draw_polygon_filled(((800, 0),
                               (800, 150),
                               (775, 220),
                               (700, 0)),
                               arcade.color.OLD_BURGUNDY)

    # Second row trees
    arcade.draw_triangle_filled(75, 0, 225, 0, 150, 120, arcade.color.FRENCH_PUCE)
    arcade.draw_triangle_filled(100, 45, 200, 45, 150, 145, arcade.color.FRENCH_PUCE)
    arcade.draw_triangle_filled(110, 95, 190, 95, 150, 170, arcade.color.FRENCH_PUCE)
    arcade.draw_triangle_filled(120, 135, 180, 135, 150, 180, arcade.color.FRENCH_PUCE)

    arcade.draw_triangle_filled(275, 0, 425, 0, 350, 170, arcade.color.FRENCH_PUCE)
    arcade.draw_triangle_filled(300, 95, 400, 95, 350, 195, arcade.color.FRENCH_PUCE)
    arcade.draw_triangle_filled(310, 135, 390, 135, 350, 220, arcade.color.FRENCH_PUCE)
    arcade.draw_triangle_filled(320, 180, 380, 180, 350, 240, arcade.color.FRENCH_PUCE)

    arcade.draw_triangle_filled(475, 0, 625, 0, 550, 120, arcade.color.FRENCH_PUCE)
    arcade.draw_triangle_filled(500, 45, 600, 45, 550, 145, arcade.color.FRENCH_PUCE)
    arcade.draw_triangle_filled(510, 95, 590, 95, 550, 170, arcade.color.FRENCH_PUCE)
    arcade.draw_triangle_filled(520, 135, 580, 135, 550, 180, arcade.color.FRENCH_PUCE)

    arcade.draw_triangle_filled(650, 0, 800, 0, 725, 170, arcade.color.FRENCH_PUCE)
    arcade.draw_triangle_filled(675, 95, 775, 95, 725, 195, arcade.color.FRENCH_PUCE)
    arcade.draw_triangle_filled(685, 135, 765, 135, 725, 220, arcade.color.FRENCH_PUCE)
    arcade.draw_triangle_filled(695, 180, 755, 180, 725, 240, arcade.color.FRENCH_PUCE)


def draw_tree(x, y):
    # First row trees
    arcade.draw_triangle_filled(x - 75, y, x + 75, y, x, y + 150, arcade.color.SEAL_BROWN)
    arcade.draw_triangle_filled(x - 50, y + 75, x + 50, y + 75, x, y + 175, arcade.color.SEAL_BROWN)
    arcade.draw_triangle_filled(x - 40, y + 125, x + 45, y + 125, x, y + 200, arcade.color.SEAL_BROWN)
    arcade.draw_triangle_filled(x - 30, y + 165, x + 30, y + 165, x, y + 210, arcade.color.SEAL_BROWN)


def draw_bridge():
    # Bridge
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, 270, 260, arcade.color.EERIE_BLACK)
    arcade.draw_line(2, 0, 2, 260, arcade.color.EERIE_BLACK, 3)
    arcade.draw_line(100, 0, 100, 260, arcade.color.EERIE_BLACK, 5)
    arcade.draw_line(200, 0, 200, 260, arcade.color.EERIE_BLACK, 5)
    arcade.draw_line(300, 0, 300, 260, arcade.color.EERIE_BLACK, 5)
    arcade.draw_line(400, 0, 400, 260, arcade.color.EERIE_BLACK, 5)
    arcade.draw_line(500, 0, 500, 260, arcade.color.EERIE_BLACK, 5)
    arcade.draw_line(600, 0, 600, 260, arcade.color.EERIE_BLACK, 5)
    arcade.draw_line(700, 0, 700, 260, arcade.color.EERIE_BLACK, 5)
    arcade.draw_line(798, 0, 798, 260, arcade.color.EERIE_BLACK, 3)
    arcade.draw_arc_outline(50, 212, 100, 100, arcade.color.EERIE_BLACK, 0, 180, 10)
    arcade.draw_arc_outline(150, 212, 100, 100, arcade.color.EERIE_BLACK, 0, 180, 10)
    arcade.draw_arc_outline(250, 212, 100, 100, arcade.color.EERIE_BLACK, 0, 180, 10)
    arcade.draw_arc_outline(350, 212, 100, 100, arcade.color.EERIE_BLACK, 0, 180, 10)
    arcade.draw_arc_outline(450, 212, 100, 100, arcade.color.EERIE_BLACK, 0, 180, 10)
    arcade.draw_arc_outline(550, 212, 100, 100, arcade.color.EERIE_BLACK, 0, 180, 10)
    arcade.draw_arc_outline(650, 212, 100, 100, arcade.color.EERIE_BLACK, 0, 180, 10)
    arcade.draw_arc_outline(750, 212, 100, 100, arcade.color.EERIE_BLACK, 0, 180, 10)


def draw_train(x, y):
    # Train
    arcade.draw_line(x - 356, y - 10, x - 100, y - 10, arcade.color.YANKEES_BLUE, 2)
    arcade.draw_rectangle_filled(x - 295, y - 3, 125, 25, arcade.color.YANKEES_BLUE)
    arcade.draw_rectangle_filled(x - 165, y - 3, 125, 25, arcade.color.YANKEES_BLUE)
    arcade.draw_polygon_filled(((x - 100, y - 15),
                                (x - 100, y + 10),
                                (x - 25, y + 10),
                                (x - 25, y + 2),
                                (x + 1, y + 2),
                                (x + 1, y - 15)),
                               arcade.color.YANKEES_BLUE)


class Balloon:
    def __init__(self, center_x, center_y, change_x, change_y, radius, color):

        self.center_x = center_x
        self.center_y = center_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

        self.error = arcade.load_sound("arcade_resources_sounds_error5.wav")

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)
        arcade.draw_rectangle_filled(self.center_x,
                                     self.center_y - (self.radius * 2),
                                     self.radius,
                                     self.radius//2,
                                     self.color)
        arcade.draw_line(self.center_x,
                         self.center_y,
                         self.center_x,
                         self.center_y - (self.radius * 2),
                         self.color,
                         1)
        arcade.draw_line(self.center_x - self.radius,
                         self.center_y,
                         self.center_x - (self.radius//2),
                         self.center_y - (self.radius * 2),
                         self.color,
                         1)
        arcade.draw_line(self.center_x + self.radius,
                         self.center_y,
                         self.center_x + (self.radius//2),
                         self.center_y - (self.radius * 2),
                         self.color,
                         1)
        arcade.draw_ellipse_filled(self.center_x,
                                   self.center_y,
                                   self.radius//1.5,
                                   self.radius * 2,
                                   arcade.color.LIBERTY)

    def update(self):
        # Move the balloon
        self.center_y += self.change_y
        self.center_x += self.change_x

        # See if the balloon hit the edge of the screen. If so, change direction
        if self.center_x < self.radius:
            arcade.play_sound(self.error)
            self.center_x = self.radius

        if self.center_x > SCREEN_WIDTH - self.radius:
            arcade.play_sound(self.error)
            self.center_x = SCREEN_WIDTH - self.radius

        if self.center_y < self.radius:
            arcade.play_sound(self.error)
            self.center_y = self.radius

        if self.center_y > SCREEN_HEIGHT - self.radius:
            arcade.play_sound(self.error)
            self.center_y = SCREEN_HEIGHT - self.radius


class Bird:
    def __init__(self, position_x, position_y, width, height, color, start_angle, end_angle, weight):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.width = width
        self.height = height
        self.color = color
        self.start_angle = start_angle
        self.end_angle = end_angle
        self.weight = weight

    def draw(self):
        arcade.draw_arc_outline(self.position_x - 7,
                                self.position_y,
                                self.width,
                                self.height,
                                self.color,
                                self.start_angle,
                                self.end_angle,
                                self.weight)
        arcade.draw_arc_outline(self.position_x + 8,
                                self.position_y,
                                self.width,
                                self.height,
                                self.color,
                                self.start_angle,
                                self.end_angle,
                                self.weight)


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        # Load the sound when the application starts
        self.crow_caw = arcade.load_sound("crow_caw.wav")

        arcade.set_background_color(arcade.color.RADICAL_RED)

        # Create bird
        self.bird = Bird(300, 400, 15, 15, arcade.color.WHITE_SMOKE, 0, 180, 3)
        self.balloon = Balloon(500, 400, 0, 0, 25, arcade.color.GRAY_BLUE)

    def on_draw(self):
        arcade.start_render()

        draw_sunset()
        draw_mountains()
        draw_background_trees()

        # First row trees
        draw_tree(75, 0)
        draw_tree(250, 0)
        draw_tree(425, 0)
        draw_tree(650, 0)

        draw_bridge()
        draw_train(300, 288)

        self.bird.draw()
        self.balloon.draw()

    def update(self, delta_time):
        self.balloon.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.balloon.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.balloon.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.balloon.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.balloon.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.balloon.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.balloon.change_y = 0

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.bird.position_x = x
        self.bird.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        """ Called when the user presses a mouse button. """

        if button == arcade.MOUSE_BUTTON_LEFT:
            print("Left mouse button pressed at", x, y)
            arcade.play_sound(self.crow_caw)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            print("Right mouse button pressed at", x, y)
            arcade.play_sound(self.crow_caw)


def main():
    window = MyGame()
    arcade.run()


main()
