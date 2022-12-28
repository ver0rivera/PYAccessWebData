
# If we want to extract data from a string in Python
#  we can use the findall() method to extract all of the substrings
# which match a regular expression.

import re
print(
    'This following program uses findall() to find the lines with email addresses in them and extract one or more addresses from each of those lines.')

s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\S+@\S+', s)
print(lst)

# The findall() method searches the string in the second argument
# and returns a list of all of the strings that look like email addresses.
# We are using a two-character sequence that matches a non-whitespace character (\\S).

print('For this new example: Let’s declare that we are only interested in the portion of the string that starts and ends with a letter or a number.')

# Square brackets are used to indicate a set of multiple acceptable
# characters we are willing to consider matching.

# Search for lines that have an at sign between characters
# The characters must be a letter or number
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    if len(x) > 0:
        print(x)
