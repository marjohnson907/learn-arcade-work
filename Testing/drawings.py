import arcade

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


def draw_astronaut(x, y):
    arcade.draw_arc_outline(x + 15, y + 5, 15, 40, arcade.color.WHITE_SMOKE, 45, 180, 5, 270)
    arcade.draw_arc_outline(x + 32, y - 5, 10, 20, arcade.color.WHITE_SMOKE, 20, 160, 5, 90)
    arcade.draw_arc_outline(x + 23, y - 16, 15, 20, arcade.color.WHITE_SMOKE, 0, 160, 5, 270)
    arcade.draw_rectangle_filled(x, y - 5, 35, 45, arcade.color.WHITE_SMOKE)
    arcade.draw_circle_outline(x, y, 15, arcade.color.WHITE_SMOKE, 5)
    arcade.draw_circle_outline(x, y, 15, arcade.color.GRAY, 1)
    arcade.draw_arc_filled(x, y - 30, 20, 40, arcade.color.WHITE_SMOKE, 0, 180)
    arcade.draw_arc_filled(x - 15, y - 30, 11, 41, arcade.color.GRAY, 0, 180, 330)
    arcade.draw_arc_filled(x + 15, y - 30, 11, 41, arcade.color.GRAY, 0, 180, 30)
    arcade.draw_lrtb_rectangle_filled(x - 10, x - 1, y - 30, y - 45, arcade.color.WHITE_SMOKE)
    arcade.draw_arc_filled(x - 10, y - 40, 10, 10, arcade.color.WHITE_SMOKE, 0, 180, 90)
    arcade.draw_lrtb_rectangle_filled(x + 1, x + 10, y - 30, y - 45, arcade.color.WHITE_SMOKE)
    arcade.draw_arc_filled(x + 10, y - 40, 10, 10, arcade.color.WHITE_SMOKE, 0, 180, 270)
    arcade.draw_arc_filled(x - 15, y - 30, 10, 40, arcade.color.WHITE_SMOKE, 0, 180, 330)
    arcade.draw_arc_filled(x - 15, y - 30, 10, 10, arcade.color.GRAY, 0, 180, 155)
    arcade.draw_arc_filled(x + 15, y - 30, 10, 40, arcade.color.WHITE_SMOKE, 0, 180, 30)
    arcade.draw_arc_filled(x + 15, y - 30, 10, 10, arcade.color.GRAY, 0, 180, 205)
    arcade.draw_circle_filled(x, y, 12, arcade.color.GRAY)


def on_draw(delta_time):
    arcade.start_render()

    draw_astronaut(250, 250)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.BLACK)

    arcade.schedule(on_draw, 1/60)

    arcade.run()


main()