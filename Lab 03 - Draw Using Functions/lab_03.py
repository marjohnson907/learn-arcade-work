import arcade

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


def draw_moon():
    # Moon
    arcade.draw_circle_filled(70, 430, 25, arcade.color.WHITE_SMOKE)
    arcade.draw_circle_filled(80, 425, 25, arcade.color.COOL_BLACK)


def draw_mountains():
    # Mountains
    arcade.draw_triangle_filled(0, 0, 350, 0, 175, 350, arcade.color.JET)
    arcade.draw_polygon_filled(((100, 0),
                               (500, 0),
                               (500, 200),
                               (350, 450)),
                               arcade.color.JET)


def draw_tree(x, y):
    # First row trees
    arcade.draw_triangle_filled(x - 75, y, x + 75, y, x, y + 150, arcade.color.DARK_JUNGLE_GREEN)
    arcade.draw_triangle_filled(x - 50, y + 75, x + 50, y + 75, x, y + 175, arcade.color.DARK_JUNGLE_GREEN)
    arcade.draw_triangle_filled(x - 40, y + 125, x + 45, y + 125, x, y + 200, arcade.color.DARK_JUNGLE_GREEN)
    arcade.draw_triangle_filled(x - 30, y + 165, x + 30, y + 165, x, y + 210, arcade.color.DARK_JUNGLE_GREEN)


def draw_star(x, y):
    # stars
    arcade.draw_point(x, y, arcade.color.WHITE, 3)


def draw_comet(x, y):
    arcade.draw_triangle_filled(x, y + 15, x, y - 15, x - 125, y, arcade.color.ELECTRIC_PURPLE)
    arcade.draw_circle_filled(x, y, 20, arcade.color.ELECTRIC_LAVENDER)
    arcade.draw_circle_filled(x, y, 15, arcade.color.PALE_MAGENTA)
    arcade.draw_circle_filled(x, y, 10, arcade.color.RAZZLE_DAZZLE_ROSE)


def on_draw(delta_time):
    arcade.start_render()

    draw_moon()

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

    draw_comet(on_draw.comet1_x, 360)
    draw_mountains()

    on_draw.comet1_x += 1

    # Second row trees
    arcade.draw_triangle_filled(75, 0, 225, 0, 150, 140, arcade.color.DARK_GREEN)
    arcade.draw_triangle_filled(100, 65, 200, 65, 150, 165, arcade.color.DARK_GREEN)
    arcade.draw_triangle_filled(110, 115, 190, 115, 150, 190, arcade.color.DARK_GREEN)
    arcade.draw_triangle_filled(120, 155, 180, 155, 150, 200, arcade.color.DARK_GREEN)

    arcade.draw_triangle_filled(275, 0, 425, 0, 350, 150, arcade.color.DARK_GREEN)
    arcade.draw_triangle_filled(300, 75, 400, 75, 350, 175, arcade.color.DARK_GREEN)
    arcade.draw_triangle_filled(310, 125, 390, 125, 350, 200, arcade.color.DARK_GREEN)
    arcade.draw_triangle_filled(320, 175, 380, 175, 350, 220, arcade.color.DARK_GREEN)

    # First row trees
    draw_tree(75, 0)
    draw_tree(250, 0)
    draw_tree(425, 0)

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

    # Train
    arcade.draw_line(0, 278, 257, 278, arcade.color.SMOKY_BLACK, 2)
    arcade.draw_rectangle_filled(60, 285, 125, 25, arcade.color.SMOKY_BLACK)
    arcade.draw_rectangle_filled(190, 285, 125, 25, arcade.color.SMOKY_BLACK)
    arcade.draw_polygon_filled(((257, 273),
                                (257, 298),
                                (332, 298),
                                (332, 290),
                                (357, 290),
                                (357, 273)),
                               arcade.color.SMOKY_BLACK)
    arcade.draw_lrtb_rectangle_filled(323, 329, 295, 291, arcade.color.ROYAL_YELLOW)
    arcade.draw_triangle_filled(356, 288, 500, 273, 500, 303, arcade.color.SUNGLOW)


on_draw.comet1_x = 0


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.COOL_BLACK)

    arcade.schedule(on_draw, 1/60)

    # Finish and run
    # arcade.finish_render()
    arcade.run()

# Call the main function
main()
