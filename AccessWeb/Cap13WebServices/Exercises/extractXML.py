
import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET

# url: http://py4e-data.dr-chuck.net/comments_1687448.xml

url = input('Please, enter the URL: ')
counter = 0
sumTotal = 0
stuff = urllib.request.urlopen(url)
ReadData = stuff.read()
tree = ET.fromstring(ReadData)
lst = tree.findall('comments/comment')

for item in lst:
    counter = counter + 1
    Tcounter = item.find('count').text
    sumTotal = sumTotal + int(Tcounter)
print('Sum:', sumTotal)
