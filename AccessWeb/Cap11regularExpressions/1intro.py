# The simplest use of the regular expression library is the search() function.

# Search for lines that contain 'From'
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)

print('Caracter especial para indicar una instruccion mas precisa')
# Adding these special characters to our regular expression
#  allow us to do sophisticated matching and extraction while writing very little code.

# Search for lines that start with 'From'
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)
