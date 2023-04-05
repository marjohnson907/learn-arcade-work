import re


# This function takes in a line of text and returns a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def main():
    """Read in the lines from a file."""

    dictionary = open("dictionary.txt")

    # Empty list to store our words
    dictionary_list = []

    # Loop through each line in the file like a list
    for line in dictionary:
        line = line.strip()
        # Add the word to the list
        dictionary_list.append(line)

    dictionary.close()


main()
