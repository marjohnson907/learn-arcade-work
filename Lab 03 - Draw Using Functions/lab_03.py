import arcade

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


def draw_moon(x, y):
    # Moon
    arcade.draw_circle_filled(x, y, 25, arcade.color.WHITE_SMOKE)
    arcade.draw_circle_filled(x + 10, y - 5, 25, arcade.color.COOL_BLACK)


def draw_mountains():
    # Mountains
    arcade.draw_triangle_filled(0, 0, 350, 0, 175, 350, arcade.color.JET)
    arcade.draw_polygon_filled(((100, 0),
                               (500, 0),
                               (500, 200),
                               (350, 450)),
                               arcade.color.JET)


def draw_background_trees():
    # Second row trees
    arcade.draw_triangle_filled(75, 0, 225, 0, 150, 120, arcade.color.DARK_GREEN)
    arcade.draw_triangle_filled(100, 45, 200, 45, 150, 145, arcade.color.DARK_GREEN)
    arcade.draw_triangle_filled(110, 95, 190, 95, 150, 170, arcade.color.DARK_GREEN)
    arcade.draw_triangle_filled(120, 135, 180, 135, 150, 180, arcade.color.DARK_GREEN)

    arcade.draw_triangle_filled(275, 0, 425, 0, 350, 170, arcade.color.DARK_GREEN)
    arcade.draw_triangle_filled(300, 95, 400, 95, 350, 195, arcade.color.DARK_GREEN)
    arcade.draw_triangle_filled(310, 135, 390, 135, 350, 220, arcade.color.DARK_GREEN)
    arcade.draw_triangle_filled(320, 180, 380, 180, 350, 240, arcade.color.DARK_GREEN)


def draw_tree(x, y):
    # First row trees
    arcade.draw_triangle_filled(x - 75, y, x + 75, y, x, y + 150, arcade.color.DARK_JUNGLE_GREEN)
    arcade.draw_triangle_filled(x - 50, y + 75, x + 50, y + 75, x, y + 175, arcade.color.DARK_JUNGLE_GREEN)
    arcade.draw_triangle_filled(x - 40, y + 125, x + 45, y + 125, x, y + 200, arcade.color.DARK_JUNGLE_GREEN)
    arcade.draw_triangle_filled(x - 30, y + 165, x + 30, y + 165, x, y + 210, arcade.color.DARK_JUNGLE_GREEN)


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


def on_draw(delta_time):
    arcade.start_render()

    draw_moon(80, 435)

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
    draw_background_trees()

    on_draw.comet1_x += 1
    on_draw.train1_x += 1

    # First row trees
    draw_tree(75, 0)
    draw_tree(250, 0)
    draw_tree(425, 0)

    draw_bridge()
    draw_train(on_draw.train1_x, 288)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.COOL_BLACK)

    arcade.schedule(on_draw, 1/60)

    # Finish and run
    # arcade.finish_render()
    arcade.run()


# Comet
on_draw.comet1_x = 0
# Train
on_draw.train1_x = 100
# Call the main function
main()
