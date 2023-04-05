"""v = "Hello there, my name is Python."
x = v.split()
print(x)"""

import re


# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

# regular expressions are a very powerful method to separate strings
