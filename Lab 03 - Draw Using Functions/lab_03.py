import arcade

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.COOL_BLACK)
    arcade.start_render()

    # Moon
    arcade.draw_circle_filled(70, 430, 25, arcade.color.WHITE_SMOKE)
    arcade.draw_circle_filled(80, 425, 25, arcade.color.COOL_BLACK)

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
    arcade.draw_triangle_filled(0, 0, 150, 0, 75, 150, arcade.color.DARK_JUNGLE_GREEN)
    arcade.draw_triangle_filled(25, 75, 125, 75, 75, 175, arcade.color.DARK_JUNGLE_GREEN)
    arcade.draw_triangle_filled(35, 125, 115, 125, 75, 200, arcade.color.DARK_JUNGLE_GREEN)
    arcade.draw_triangle_filled(45, 165, 105, 165, 75, 210, arcade.color.DARK_JUNGLE_GREEN)

    arcade.draw_triangle_filled(175, 0, 325, 0, 250, 150, arcade.color.DARK_JUNGLE_GREEN)
    arcade.draw_triangle_filled(200, 75, 300, 75, 250, 175, arcade.color.DARK_JUNGLE_GREEN)
    arcade.draw_triangle_filled(210, 125, 290, 125, 250, 200, arcade.color.DARK_JUNGLE_GREEN)
    arcade.draw_triangle_filled(220, 165, 280, 165, 250, 210, arcade.color.DARK_JUNGLE_GREEN)

    arcade.draw_triangle_filled(350, 0, 500, 0, 425, 150, arcade.color.DARK_JUNGLE_GREEN)
    arcade.draw_triangle_filled(375, 75, 475, 75, 425, 175, arcade.color.DARK_JUNGLE_GREEN)
    arcade.draw_triangle_filled(385, 125, 465, 125, 425, 200, arcade.color.DARK_JUNGLE_GREEN)
    arcade.draw_triangle_filled(395, 165, 455, 165, 425, 210, arcade.color.DARK_JUNGLE_GREEN)

    # Bridge
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, 250, 230, arcade.color.EERIE_BLACK)

    # Finish and run
    arcade.finish_render()
    arcade.run()

# Call the main function
main()
