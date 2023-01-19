import arcade

arcade.open_window(600, 600, "Lab 2")
arcade.set_background_color(arcade.csscolor.LIGHT_BLUE)

arcade.start_render()

# background
arcade.draw_circle_filled(120, 380, 100, arcade.csscolor.DARK_GREEN)
arcade.draw_circle_filled(10, 300, 100, arcade.csscolor.FOREST_GREEN)
arcade.draw_circle_filled(525, 350, 50, arcade.csscolor.DARK_GREEN)
arcade.draw_circle_filled(575, 300, 60, arcade.csscolor.FOREST_GREEN)
arcade.draw_polygon_filled(((0, 0),
                            (0, 300),
                            (300, 599),
                            (599, 300),
                            (599, 0)
                            ),
                           arcade.csscolor.BEIGE)

# woman
arcade.draw_rectangle_filled(150, 325, 40, 100, arcade.csscolor.WHEAT)
arcade.draw_ellipse_filled(150, 390, 125, 175, arcade.csscolor.WHEAT)
arcade.draw_arc_outline(150, 390, 100, 150, arcade.csscolor.YELLOW, 0, 90, 50)

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
arcade.draw_rectangle_filled(450, 350, 50, 150, arcade.csscolor.WHEAT)
arcade.draw_ellipse_filled(450, 420, 150, 210, arcade.csscolor.WHEAT)
arcade.draw_rectangle_filled(450, 140, 300, 280, arcade.csscolor.NAVY)
arcade.draw_rectangle_filled(450, 140, 125, 280, arcade.csscolor.WHITE)
arcade.draw_rectangle_filled(450, 100, 125, 200, arcade.csscolor.SKY_BLUE)
arcade.draw_circle_outline(420, 435, 25, arcade.csscolor.GRAY)
arcade.draw_circle_outline(480, 435, 25, arcade.csscolor.GRAY)
arcade.draw_line(444, 435, 456, 435, arcade.csscolor.GRAY)
arcade.draw_line(310, 150, 420, 150, arcade.csscolor.BLACK, 3)
arcade.draw_line(310, 150, 310, 350, arcade.csscolor.BLACK, 3)
arcade.draw_line(420, 150, 420, 350, arcade.csscolor.BLACK, 3)
arcade.draw_line(365, 0, 365, 350, arcade.csscolor.BLACK, 3)

arcade.finish_render()

arcade.run()
