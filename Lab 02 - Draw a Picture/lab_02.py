import arcade

arcade.open_window(600, 600, "Lab 2")
arcade.set_background_color(arcade.csscolor.LIGHT_BLUE)

arcade.start_render()

# background
arcade.draw_circle_filled(120, 380, 100, arcade.csscolor.DARK_GREEN)
arcade.draw_circle_filled(10, 300, 100, arcade.csscolor.FOREST_GREEN)
arcade.draw_circle_filled(525, 350, 50, arcade.csscolor.DARK_GREEN)
arcade.draw_circle_filled(575, 300, 60, arcade.csscolor.FOREST_GREEN)

# house
arcade.draw_polygon_filled(((0, 0),
                            (0, 300),
                            (300, 599),
                            (599, 300),
                            (599, 0)),
                           arcade.csscolor.BEIGE)
arcade.draw_line(300, 590, 300, 550, arcade.csscolor.BISQUE, 2)
arcade.draw_line(300, 400, 300, 375, arcade.csscolor.BISQUE, 2)
arcade.draw_line(210, 500, 210, 375, arcade.csscolor.BISQUE, 2)
arcade.draw_line(240, 530, 240, 375, arcade.csscolor.BISQUE, 2)
arcade.draw_line(270, 400, 270, 375, arcade.csscolor.BISQUE, 2)
arcade.draw_line(270, 535, 270, 560, arcade.csscolor.BISQUE, 2)
arcade.draw_line(330, 535, 330, 560, arcade.csscolor.BISQUE, 2)
arcade.draw_line(330, 400, 330, 375, arcade.csscolor.BISQUE, 2)
arcade.draw_line(360, 530, 360, 375, arcade.csscolor.BISQUE, 2)
arcade.draw_line(390, 500, 390, 375, arcade.csscolor.BISQUE, 2)
arcade.draw_line(10, 300, 300, 590, arcade.csscolor.DARK_KHAKI, 2)
arcade.draw_line(300, 590, 590, 300, arcade.csscolor.DARK_KHAKI, 2)
arcade.draw_line(0, 300, 300, 599, arcade.csscolor.DARK_GRAY, 4)
arcade.draw_line(599, 300, 300, 599, arcade.csscolor.DARK_GRAY, 4)
arcade.draw_parabola_outline(250, 325, 350, 150, arcade.csscolor.DARK_GRAY, 4)
arcade.draw_line(250, 475, 250, 400, arcade.csscolor.DARK_GRAY, 2)
arcade.draw_line(250, 400, 350, 400, arcade.csscolor.DARK_GRAY, 2)
arcade.draw_line(350, 475, 350, 400, arcade.csscolor.DARK_GRAY, 2)
arcade.draw_lrtb_rectangle_filled(303, 345, 470, 405, arcade.csscolor.DARK_GRAY)
arcade.draw_lrtb_rectangle_filled(255, 299, 470, 405, arcade.csscolor.DARK_GRAY)
arcade.draw_triangle_filled(255, 475, 299, 475, 277, 530, arcade.csscolor.DARK_GRAY)
arcade.draw_triangle_filled(345, 475, 301, 475, 323, 530, arcade.csscolor.DARK_GRAY)
arcade.draw_polygon_filled(((300, 545),
                            (320, 530),
                            (300, 480),
                            (280, 530)),
                           arcade.csscolor.DARK_GRAY)
arcade.draw_polygon_filled(((0, 300),
                            (75, 375),
                            (525, 375),
                            (599, 300)),
                           arcade.csscolor.DARK_GRAY)

# woman head
arcade.draw_rectangle_filled(150, 325, 40, 100, arcade.csscolor.WHEAT)
arcade.draw_ellipse_filled(150, 390, 125, 175, arcade.csscolor.WHEAT)
arcade.draw_arc_outline(150, 390, 100, 150, arcade.csscolor.YELLOW, 0, 180, 50)

# woman body
arcade.draw_polygon_filled(((0, 0),
                           (0, 225),
                           (100, 280),
                           (200, 280),
                           (300, 225),
                           (300, 0)),
                           arcade.csscolor.BLACK)
arcade.draw_polygon_filled(((25, 0),
                            (25, 240),
                            (50, 253),
                            (100, 215),
                            (150, 200),
                            (200, 215),
                            (250, 253),
                            (275, 240),
                            (275, 0)),
                           arcade.csscolor.SADDLE_BROWN)
arcade.draw_line(50, 253, 100, 215, arcade.csscolor.DARK_KHAKI, 3)
arcade.draw_line(100, 215, 150, 200, arcade.csscolor.DARK_KHAKI, 3)
arcade.draw_line(150, 200, 200, 215, arcade.csscolor.DARK_KHAKI, 3)
arcade.draw_line(200, 215, 250, 253, arcade.csscolor.DARK_KHAKI, 3)
arcade.draw_triangle_filled(100, 280, 200, 280, 150, 250, arcade.csscolor.WHITE)
arcade.draw_circle_filled(150, 265, 15, arcade.csscolor.GOLD)

# man head
arcade.draw_rectangle_filled(450, 350, 50, 150, arcade.csscolor.WHEAT)
arcade.draw_ellipse_filled(450, 420, 150, 210, arcade.csscolor.WHEAT)

# man body
arcade.draw_rectangle_filled(450, 140, 300, 280, arcade.csscolor.MIDNIGHT_BLUE)
arcade.draw_rectangle_filled(450, 140, 125, 280, arcade.csscolor.WHITE)
arcade.draw_rectangle_filled(450, 100, 125, 200, arcade.csscolor.SKY_BLUE)
arcade.draw_line(500, 200, 500, 280, arcade.csscolor.SKY_BLUE)
arcade.draw_line(495, 200, 495, 280, arcade.csscolor.SKY_BLUE)
arcade.draw_line(490, 200, 490, 280, arcade.csscolor.SKY_BLUE)
arcade.draw_line(445, 200, 445, 280, arcade.csscolor.SKY_BLUE)
arcade.draw_line(450, 200, 450, 280, arcade.csscolor.SKY_BLUE)
arcade.draw_line(455, 200, 455, 280, arcade.csscolor.SKY_BLUE)
arcade.draw_line(415, 200, 415, 280, arcade.csscolor.SKY_BLUE)
arcade.draw_line(410, 200, 410, 280, arcade.csscolor.SKY_BLUE)
arcade.draw_line(405, 200, 405, 280, arcade.csscolor.SKY_BLUE)

# man glasses
arcade.draw_circle_outline(420, 435, 25, arcade.csscolor.GRAY)
arcade.draw_circle_outline(480, 435, 25, arcade.csscolor.GRAY)
arcade.draw_line(444, 435, 456, 435, arcade.csscolor.GRAY)

# man pitchfork
arcade.draw_line(310, 150, 420, 150, arcade.csscolor.BLACK, 3)
arcade.draw_line(310, 150, 310, 350, arcade.csscolor.BLACK, 3)
arcade.draw_line(420, 150, 420, 350, arcade.csscolor.BLACK, 3)
arcade.draw_line(365, 0, 365, 350, arcade.csscolor.BLACK, 3)

arcade.finish_render()

arcade.run()
