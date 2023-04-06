import re


# This function takes in a line of text and returns a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def read_in_file(file_name):

    # Open the file for reading
    my_file = open(file_name)

    # Create an empty list to store the dictionary
    dictionary_list = []

    # Loop through each line in the file like a list
    for line in my_file:
        # Remove any line feed, carriage returns or spaces at the end of the line
        line = line.strip()
        # Add the name to the list
        dictionary_list.append(line)

    my_file.close()

    return dictionary_list


def main():

    dictionary = read_in_file("dictionary.txt")

    alice_wonderland = open("AliceInWonderLand200.txt")

    print("---Linear Search---")

    for line in alice_wonderland:
        line = line.strip()
        word_list = split_line(line)

        for word in word_list:
            word = split_line(word.upper())

            current_list_position = 0

            while current_list_position < 200:
                current_list_position += 1
                if word != dictionary:
                    print("possible misspelled word: ", word)

    alice_wonderland.close()


main()
