class Character:
    def __init__(self):
        self.name = ""
        self.outfit = ""
        self.max_hit_points = 0
        self.current_hit_points = 0
        self.armor_amount = 0
        self.max_speed = 0


class Address:
    def __init__(self):
        self.name = ""
        self.line1 = ""
        self.line2 = ""
        self.city = ""
        self.state = ""
        self.zip = ""

def print_address(address):
    """ Print an address to the screen """

    print(address.name)
    # If there is a line1 in the address, print it
    if len(address.line1) > 0:
        print(address.line1)
    # If there is a line2 in the address, print it
    if len(address.line2) > 0:
        print( address.line2 )
    print(address.city + ", " + address.state + " " + address.zip)

def main():
    home_address = Address()

    home_address.name = "John Smith"
    home_address.line1 = "701 N. C Street"
    home_address.line2 = "Carver Science Building"
    home_address.city = "Indianola"
    home_address.state = "IA"
    home_address.zip = "50125"

    # Create another address
    vacation_home_address = Address()

    # Set the fields in the address
    vacation_home_address.name = "John Smith"
    vacation_home_address.line1 = "1122 Main Street"
    vacation_home_address.line2 = ""
    vacation_home_address.city = "Panama City Beach"
    vacation_home_address.state = "FL"
    vacation_home_address.zip = "32407"

    print("The client's main home is in " + home_address.city)
    print("His vacation home is in " + vacation_home_address.city)

    print_address(home_address)
    print()
    print_address(vacation_home_address)



main()