import urllib.request
import urllib.parse
import urllib.error

print('LIKE A FILE')

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

# Again, once we have opened the web page, we can read it like a local file.
