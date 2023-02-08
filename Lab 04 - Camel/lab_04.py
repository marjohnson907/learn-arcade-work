import arcade

miles_traveled = 0
thirst = 0
camel_tired = 0
canteen_drinks = 3
natives_distance = -20


def main():
    print("Welcome to Camel!")
    print("""You have stolen a camel to make your way across the great Mobi desert.
The natives want their camel back and are chasing you down! 
Survive your desert trek and out run the natives.""")

    done = False
    while not done:
        print("""A. Drink from your canteen.
B. Ahead moderate speed.
C. Ahead full speed.
D. Stop for the night.
E. Status check.
Q. Quit.""")

        user_choice = input("What is your choice? ")
        if user_choice.upper() == "Q":
            print("You have quit.")
            done = True
        elif user_choice.upper() == "D":
            camel_tired = 0
            print("Your camel is happy.")
            natives_distance = natives_distance + 13
            print("The natives are ", miles_traveled - natives_distance, " miles behind you.")
        elif user_choice.upper() == "C":
            miles_traveled = miles_traveled + 12
            print(miles_traveled)
            thirst = thirst + 1
            camel_tired = camel_tired + 2
            natives_distance = natives_distance + 13
            print("The natives are ",miles_traveled - natives_distance, "miles behind you.")
            done = True




main()