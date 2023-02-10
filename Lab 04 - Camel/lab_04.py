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

        elif user_choice.upper() == "E":
            print("You have traveled ", miles_traveled, " miles.")
            print("Drinks in canteen: ", canteen_drinks)
            print("The natives are ", (miles_traveled - natives_distance), "miles behind you.")

        elif user_choice.upper() == "D":
            camel_tired = 0
            print("Your camel is happy.")
            print("The natives are ", miles_traveled - (natives_distance + random.randint(7, 14)), " miles behind you.")

        elif user_choice.upper() == "C":
            print("You have traveled ", miles_traveled + random.randint(10, 20), " miles.")
            thirst = thirst + 1
            camel_tired = camel_tired + random.randint(1, 3)
            print("The natives are ",miles_traveled - (natives_distance + random.randint(7, 14)), "miles behind you.")

        elif user_choice.upper() == "B":
            print("You have traveled ", miles_traveled + random.randint(5, 12), " miles.")
            thirst = thirst + 1
            camel_tired = camel_tired + 1
            print("The natives are ", miles_traveled - (natives_distance + random.randint(7, 14)), "miles behind you.")

        elif user_choice.upper() == "A":
            if canteen_drinks >= 1:
                thirst = 0
                canteen_drinks = canteen_drinks - 1
            elif canteen_drinks < 1:
                print("Your canteen is dry.")

        if thirst > 4:
            print("You are thirsty.")
        elif thirst > 6:
            print("You died of thirst!")
            done = True

        if camel_tired >= 5:
            print("Your camel is tired.")
        elif camel_tired > 8:
            print("Your camel is dead.")
            done = True

        if miles_traveled - natives_distance < 15:
            print("The natives are getting close!")
        elif miles_traveled - natives_distance < 1:
            print("The natives caught you.")
            done = True

        if miles_traveled >= 200:
            print("You won the game!")
            done = True








main()