import random


def main():
    print("Welcome to Camel!")
    print("""You have stolen a camel to make your way across the great Mobi desert.
The natives want their camel back and are chasing you down! 
Survive your desert trek and out run the natives.""")

    miles_traveled = 0
    thirst = 0
    camel_tired = 0
    canteen_drinks = 3
    natives_distance = -20

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

        elif user_choice.upper() == "A":
            if canteen_drinks >= 1:
                thirst = 0
                canteen_drinks = canteen_drinks - 1
            elif canteen_drinks < 1:
                print("Your canteen is dry.")

        elif user_choice.upper() == "B":
            miles_traveled = miles_traveled + random.randint(5, 12)
            print("You have traveled ", miles_traveled, " miles.")
            thirst = thirst + 1
            camel_tired = camel_tired + 1
            natives_distance = natives_distance + random.randint(7, 14)
            print("The natives are ", miles_traveled - natives_distance, "miles behind you.")
            if random.randrange(21) == 1:
                print("You have found an oasis!")
                thirst = 0
                camel_tired = 0
                canteen_drinks = 5

        elif user_choice.upper() == "C":
            miles_traveled = miles_traveled + random.randint(10, 20)
            print("You have traveled ", miles_traveled, " miles.")
            thirst = thirst + 1
            camel_tired = camel_tired + random.randint(1, 3)
            natives_distance = natives_distance + random.randint(7, 14)
            print("The natives are ", miles_traveled - natives_distance, "miles behind you.")
            if random.randrange(21) == 1:
                print("You have found an oasis!")
                thirst = 0
                camel_tired = 0
                canteen_drinks = 5

        elif user_choice.upper() == "D":
            camel_tired = 0
            print("Your camel is happy.")
            natives_distance = natives_distance + random.randint(7, 14)
            print("The natives are ", miles_traveled - natives_distance, "miles behind you.")

        elif user_choice.upper() == "E":
            print("You have traveled ", miles_traveled, " miles.")
            print("Drinks in canteen: ", canteen_drinks)
            print("The natives are ", (miles_traveled - natives_distance), "miles behind you.")

        if not done and miles_traveled - natives_distance < 15 and miles_traveled - natives_distance > 1:
            print("The natives are getting close!")
        elif not done and miles_traveled - natives_distance < 1:
            print("The natives caught you.")
            done = True

        if not done and thirst > 4 and thirst <= 6:
            print("You are thirsty.")
        elif not done and thirst > 6:
            print("You died of thirst!")
            done = True

        if not done and camel_tired >= 5 and camel_tired <= 8:
            print("Your camel is tired.")
        elif not done and camel_tired > 8:
            print("Your camel is dead.")
            done = True

        if not done and miles_traveled >= 200:
            print("You won the game!")
            done = True


main()