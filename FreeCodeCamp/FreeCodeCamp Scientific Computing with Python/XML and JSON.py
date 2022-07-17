import xml.etree.ElementTree as ET
import json

data = ''' <person>
    <name>Chuck</name>
    <phone type="intl">+1 734 303 4456</phone>
    <email hide="yes"/>
    </person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))


input = '''[
    { "id" : "001",
      "x" : "2",
      "name" : "Chuck"
      },
      { "id" : "009",
      "x" : "7",
      "name" : "Ben"
      }]'''

info = json.loads(input)
print('User count:', len(info))
for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])

print(info[1]['name'])