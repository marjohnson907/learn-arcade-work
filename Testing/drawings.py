import arcade

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


def draw_astronaut(x, y):
    arcade.draw_circle_outline(x, y, 12, arcade.color.WHITE_SMOKE, 3)
    arcade.draw_circle_filled(x, y, 10, arcade.color.GRAY)
    arcade.draw_arc_filled(x, y - 30, 20, 40, arcade.color.WHITE_SMOKE, 0, 180)
    arcade.draw_lrtb_rectangle_filled(x - 10, x - 1, y - 30, y - 40, arcade.color.WHITE_SMOKE)
    arcade.draw_lrtb_rectangle_filled(x + 1, x + 10, y - 30, y - 40, arcade.color.WHITE_SMOKE)
    arcade.draw_arc_filled(x - 15, y - 30, 10, 40, arcade.color.WHITE_SMOKE, 0, 180, 330)
    arcade.draw_arc_filled(x + 15, y - 30, 10, 40, arcade.color.WHITE_SMOKE, 0, 180, 30)


def on_draw(delta_time):
    arcade.start_render()

    draw_astronaut(250, 250)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.BLACK)

    arcade.schedule(on_draw, 1/60)

    arcade.run()


main()