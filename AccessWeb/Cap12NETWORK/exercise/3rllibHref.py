import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# try with http://py4e-data.dr-chuck.net/known_by_Naisha.html
url = input('enter url')
# position 18
link_line = int(input('enter posicion')) - 1
# numer 7
urlCounters = int(input('enter times'))

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

while urlCounters >= 0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    print(url)
    url = tags[link_line].get("href", None)
    urlCounters = urlCounters - 1
