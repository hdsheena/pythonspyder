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

#put_rows_together()

dates = []
content = []
for item in just_data:
   if "test" in item.keys():
       dates.append(item['test'])
   else:
    content.append(item['date'])
    
print content[0], dates [0]
dictionary_of_metadata = {}
list_of_threads = []
list_of_post_numbers = []
#make dates string into time stamp and topic heading
for item in dates:
    print item
    string = item[0]
    print string
    date_string = string.replace('#', 'to:')
    print "Splitting"
    
    split_string = date_string.split('to:')
    print split_string[1], split_string[2]
    name_of_thread = split_string[1][1:-1]
    post_number = split_string[2]
    print name_of_thread, post_number
    list_of_threads.append(name_of_thread)
    list_of_post_numbers.append(post_number)
    dictionary_of_metadata[name_of_thread] = post_number
    
print list_of_threads
def make_new_dictionary():
    for item in content:
        new_value = {}
        print item
        number_of_item = content.index(item)
        print number_of_item
        value = item[0]
        key = list_of_threads[number_of_item]
        post_number = list_of_post_numbers[number_of_item]
        new_value[post_number] = value
        print key
        new_data.setdefault(key,[]).append(new_value)
    
def thread_to_file(value, key):
    filename = str(key)+".json"
    with open(filename, 'w') as outfile:
        json.dump(value, outfile)
make_new_dictionary()
for key in new_data.keys():
    thread = new_data[key]
    thread_to_file(thread, key)
#print dictionary_of_metadata