import xml.etree.ElementTree as ET

# Here is a simple application that parses some XML
#  and extracts some data elements from the XML:

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

# The find function searches through the XML
# tree and retrieves a node that matches the specified tag.
#
# Each node can have some text, some attributes (like hide),
# and some “child” nodes.
#
# Each node can be the top of a tree of nodes.

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
