import arcade

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
arcade.set_background_color(arcade.color.COOL_BLACK)
arcade.start_render()

# Moon
arcade.draw_circle_filled(70, 430, 25, arcade.color.WHITE_SMOKE)
arcade.draw_circle_filled(80, 425, 25, arcade.color.COOL_BLACK)

# Finish and run
arcade.finish_render()
arcade.run()

