import json
import sys

file = open('joyride2.json', 'rb')
data = json.loads(file.read())

just_data = data['data']

new_data = {}


def put_rows_together():
    for item in just_data:
         print item.keys()
         try:
            date = item['test']
         except:
            content = item['date']
    #new_data[date] = content

put_rows_together()

dates = []
content = []
for item in just_data:
   if "test" in item.keys():
       dates.append(item['test'])
   else:
    content.append(item['date'])
    
print content[0], dates [0]