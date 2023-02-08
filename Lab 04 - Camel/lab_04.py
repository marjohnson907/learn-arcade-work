import arcade


def main():
    print("Welcome to Camel!")
    print("""You have stolen a camel to make your way across the great Mobi desert.
The natives want their camel back and are chasing you down! 
Survive your desert trek and out run the natives.""")

    miles_traveled = 0
    thirst = 0
    camel_tired = 0

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




main()