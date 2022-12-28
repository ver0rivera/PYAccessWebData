import urllib.request
import urllib.parse
import urllib.error
import json
# url: http://py4e-data.dr-chuck.net/comments_1687449.json
url = input('Please, enter the URL: ')
counter = 0
sumTotal = 0
stuff = urllib.request.urlopen(url)
ReadData = stuff.read()
info = json.loads(ReadData)
data = info.get('comments')
totalData = range(len(data))

for i in totalData:
    counter = counter+1
    rangData = data[i]
    extract = rangData.get('count')
    sumTotal = sumTotal + int(extract)
print('Sum:', sumTotal)
