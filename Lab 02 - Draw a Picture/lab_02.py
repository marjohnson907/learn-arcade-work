import arcade

arcade.open_window(600, 600, "Lab 2")
arcade.set_background_color(arcade.csscolor.LIGHT_BLUE)

arcade.start_render()

# background
arcade.draw_circle_filled(120, 380, 100, arcade.csscolor.DARK_GREEN)
arcade.draw_polygon_filled(((0, 0),
                            (0, 300),
                            (300, 599),
                            (599, 300),
                            (599, 0)
                            ),
                           arcade.csscolor.BEIGE)

# woman
arcade.draw_rectangle_filled(150, 325, 25, 100, arcade.csscolor.WHEAT)
arcade.draw_ellipse_filled(150, 375, 100, 150, arcade.csscolor.WHEAT)
arcade.draw_polygon_filled(((0, 0),
                           (0, 225),
                           (100, 280),
                           (200, 280),
                           (300, 225),
                           (300, 0)
                            ),
                           arcade.csscolor.DARK_BLUE)
arcade.draw_polygon_filled(((25, 0),
                            (25, 240),
                            (70, 265),
                            (150, 250),
                            (225, 265),
                            (275, 240),
                            (275, 0)
                            ),
                           arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(100, 280, 200, 280, 150, 250, arcade.csscolor.WHITE)
arcade.draw_circle_filled(150, 265, 15, arcade.csscolor.GOLD)

# man
arcade.draw_rectangle_filled(450, 350, 25, 150, arcade.csscolor.WHEAT)
arcade.draw_ellipse_filled(450, 400, 125, 175, arcade.csscolor.WHEAT)
arcade.draw_rectangle_filled(450, 140, 300, 280, arcade.csscolor.NAVY)
arcade.draw_rectangle_filled(450, 140, 150, 280, arcade.csscolor.WHITE)
arcade.draw_rectangle_filled(450, 100, 150, 200, arcade.csscolor.SKY_BLUE)

arcade.finish_render()

arcade.run()
