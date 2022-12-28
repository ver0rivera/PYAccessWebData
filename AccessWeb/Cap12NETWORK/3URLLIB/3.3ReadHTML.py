import urllib.request
import urllib.parse
import urllib.error

# Read an HTML and print it

print('READ AN HTML')
fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')

for line in fhand:
    print(line.decode().strip())
