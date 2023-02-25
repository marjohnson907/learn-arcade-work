# variables
#       Class: attributes (variables) & methods (functions)
# functions
# code

# What is the difference between placing attributes inside parentheses versus the self.attribute = "whatever"

class Character:
    def __init__(self, p_first_name, p_last_name, p_outfit):
        self.first_name = p_first_name
        self.last_name = p_last_name
        self.outfit = p_outfit
        self.max_hit_points = 0
        self.current_hit_points = 0
        self.armor_amount = 0
        self.max_speed = 0

    def set_outfit_color(self, p_color):
        self.outfit = self.outfit + " Color: " + p_color

first_name = 'no, it is not.'
Bob = Character("Bob", "Ross", "Painter Pants")
char1 = Character("Sue", "Someone", "Mechanic Overalls")
print("Name:", Bob.first_name, Bob.last_name)
Bob.set_outfit_color("Blue")

print("Outfit:", Bob.outfit)
print("Name:", first_name)

x = 3
print("x =", x, "and is of type:", type(x))

x = 3.145
print("x =", x, "and is of type:", type(x))

x = "Hi there"
print("x =", x, "and is of type:", type(x))

x = True
print("x =", x, "and is of type:", type(x))