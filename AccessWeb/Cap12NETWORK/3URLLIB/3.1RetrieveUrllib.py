import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

# Once the web page has been opened with urllib.urlopen,
# we can treat it like a file and read through it using a for loop.
