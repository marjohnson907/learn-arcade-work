""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_moon(x, y):
    # Moon
    arcade.draw_circle_filled(x, y, 25, arcade.color.WHITE_SMOKE)
    arcade.draw_circle_filled(x + 10, y - 5, 25, arcade.color.BLACK)


def draw_mountains():
    # Mountains
#    arcade.draw_triangle_filled(0, 0, 400, 0, 200, 400, arcade.color.GRAPE)
    arcade.draw_triangle_filled(0, 0, 350, 0, 175, 350, arcade.color.FRENCH_LILAC)
    arcade.draw_triangle_filled(175, 0, 575, 0, 375, 500, arcade.color.FRENCH_LILAC)
    arcade.draw_triangle_filled(400, 0, 800, 0, 600, 400, arcade.color.FRENCH_LILAC)


def draw_background_trees():
    # Second row trees
    arcade.draw_triangle_filled(75, 0, 225, 0, 150, 120, arcade.color.KOMBU_GREEN)
    arcade.draw_triangle_filled(100, 45, 200, 45, 150, 145, arcade.color.KOMBU_GREEN)
    arcade.draw_triangle_filled(110, 95, 190, 95, 150, 170, arcade.color.KOMBU_GREEN)
    arcade.draw_triangle_filled(120, 135, 180, 135, 150, 180, arcade.color.KOMBU_GREEN)

    arcade.draw_triangle_filled(275, 0, 425, 0, 350, 170, arcade.color.KOMBU_GREEN)
    arcade.draw_triangle_filled(300, 95, 400, 95, 350, 195, arcade.color.KOMBU_GREEN)
    arcade.draw_triangle_filled(310, 135, 390, 135, 350, 220, arcade.color.KOMBU_GREEN)
    arcade.draw_triangle_filled(320, 180, 380, 180, 350, 240, arcade.color.KOMBU_GREEN)

    arcade.draw_triangle_filled(475, 0, 625, 0, 550, 120, arcade.color.KOMBU_GREEN)
    arcade.draw_triangle_filled(500, 45, 600, 45, 550, 145, arcade.color.KOMBU_GREEN)
    arcade.draw_triangle_filled(510, 95, 590, 95, 550, 170, arcade.color.KOMBU_GREEN)
    arcade.draw_triangle_filled(520, 135, 580, 135, 550, 180, arcade.color.KOMBU_GREEN)

    arcade.draw_triangle_filled(650, 0, 800, 0, 725, 170, arcade.color.KOMBU_GREEN)
    arcade.draw_triangle_filled(675, 95, 775, 95, 725, 195, arcade.color.KOMBU_GREEN)
    arcade.draw_triangle_filled(685, 135, 765, 135, 725, 220, arcade.color.KOMBU_GREEN)
    arcade.draw_triangle_filled(695, 180, 755, 180, 725, 240, arcade.color.KOMBU_GREEN)

def draw_tree(x, y):
    # First row trees
    arcade.draw_triangle_filled(x - 75, y, x + 75, y, x, y + 150, arcade.color.LA_SALLE_GREEN)
    arcade.draw_triangle_filled(x - 50, y + 75, x + 50, y + 75, x, y + 175, arcade.color.LA_SALLE_GREEN)
    arcade.draw_triangle_filled(x - 40, y + 125, x + 45, y + 125, x, y + 200, arcade.color.LA_SALLE_GREEN)
    arcade.draw_triangle_filled(x - 30, y + 165, x + 30, y + 165, x, y + 210, arcade.color.LA_SALLE_GREEN)


def draw_bridge():
    # Bridge
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, 270, 260, arcade.color.EERIE_BLACK)
    arcade.draw_line(2, 0, 2, 260, arcade.color.EERIE_BLACK, 3)
    arcade.draw_line(100, 0, 100, 260, arcade.color.EERIE_BLACK, 5)
    arcade.draw_line(200, 0, 200, 260, arcade.color.EERIE_BLACK, 5)
    arcade.draw_line(300, 0, 300, 260, arcade.color.EERIE_BLACK, 5)
    arcade.draw_line(400, 0, 400, 260, arcade.color.EERIE_BLACK, 5)
    arcade.draw_line(498, 0, 498, 260, arcade.color.EERIE_BLACK, 3)
    arcade.draw_arc_outline(50, 212, 100, 100, arcade.color.EERIE_BLACK, 0, 180, 10)
    arcade.draw_arc_outline(150, 212, 100, 100, arcade.color.EERIE_BLACK, 0, 180, 10)
    arcade.draw_arc_outline(250, 212, 100, 100, arcade.color.EERIE_BLACK, 0, 180, 10)
    arcade.draw_arc_outline(350, 212, 100, 100, arcade.color.EERIE_BLACK, 0, 180, 10)
    arcade.draw_arc_outline(450, 212, 100, 100, arcade.color.EERIE_BLACK, 0, 180, 10)


def draw_train(x, y):
    # Train
    arcade.draw_line(x- 356, y - 10, x - 100, y - 10, arcade.color.SMOKY_BLACK, 2)
    arcade.draw_rectangle_filled(x - 295, y - 3, 125, 25, arcade.color.SMOKY_BLACK)
    arcade.draw_rectangle_filled(x - 165, y - 3, 125, 25, arcade.color.SMOKY_BLACK)
    arcade.draw_polygon_filled(((x - 100, y - 15),
                                (x - 100, y + 10),
                                (x - 25, y + 10),
                                (x - 25, y + 2),
                                (x + 1, y + 2),
                                (x + 1, y - 15)),
                               arcade.color.SMOKY_BLACK)
    arcade.draw_triangle_filled(x, y, x + 140, y - 15, x + 140, y + 15, arcade.color.SUNGLOW)


def draw_star(x, y):
    # stars
    arcade.draw_point(x, y, arcade.color.WHITE, 3)


def draw_comet(x, y):
    arcade.draw_triangle_filled(x, y + 15, x, y - 15, x - 125, y, arcade.color.ELECTRIC_PURPLE)
    arcade.draw_circle_filled(x, y, 20, arcade.color.ELECTRIC_LAVENDER)
    arcade.draw_circle_filled(x, y, 15, arcade.color.PALE_MAGENTA)
    arcade.draw_circle_filled(x, y, 10, arcade.color.RAZZLE_DAZZLE_ROSE)


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

    def on_draw(self):
        arcade.start_render()

        draw_moon(100, 535)

        # Stars
        draw_star(80, 330)
        draw_star(20, 355)
        draw_star(35, 222)
        draw_star(23, 100)
        draw_star(130, 400)
        draw_star(209, 480)
        draw_star(272, 412)
        draw_star(250, 325)
        draw_star(416, 477)
        draw_star(482, 425)
        draw_star(458, 319)
        draw_star(580, 330)
        draw_star(620, 555)
        draw_star(735, 422)
        draw_star(523, 600)
        draw_star(730, 400)
        draw_star(609, 380)
        draw_star(572, 412)
        draw_star(250, 325)
        draw_star(416, 477)
        draw_star(482, 425)
        draw_star(458, 319)

        draw_comet(200, 360)
        draw_mountains()
        draw_background_trees()

        # First row trees
        draw_tree(75, 0)
        draw_tree(250, 0)
        draw_tree(425, 0)
        draw_tree(650, 0)

        draw_bridge()
        draw_train(300, 288)


def main():
    window = MyGame()
    arcade.run()


main()