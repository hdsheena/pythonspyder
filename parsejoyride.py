import json
import sys
from text_unidecode import unidecode 

file = open('joyride2.json', 'rb')
data = json.loads(file.read())

just_data = data['data']

new_data = {}

def make_list_better(list_item):
    print list_item[0][0]
    better = unidecode(list_item)
    print list_item[0]
    print better
    return better
    
    
def put_rows_together():
    for item in just_data:
         #print item.keys()
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
        to_dates = item['test']
        #print to_dates[0]
        dates.append(to_dates[0])
    else:
        to_content = item['date']
        
        content.append(to_content[0])
        
new_content = []
for item in content:
    print "____________________________$$$$$_____________"
    print item    
    new_item = make_list_better(item)
    
    new_content.append(new_item)
    
content_variable = content[1]
print content_variable
content_variable_string = content_variable.encode('utf-8')

print content[0], "DATES", dates [0]
dictionary_of_metadata = {}
list_of_threads = []
list_of_post_numbers = []
#make dates string into time stamp and topic heading
for item in dates:
    #print item
    string = item
    #print string
    date_string = string.replace('#', 'to:')
    #print "Splitting"

    split_string = date_string.split('to:')
    #print split_string[1], split_string[2]
    name_of_thread = split_string[1][1:-1]
    post_number = split_string[2]
    #print name_of_thread, post_number
    list_of_threads.append(name_of_thread)
    list_of_post_numbers.append(post_number)
    dictionary_of_metadata[name_of_thread] = post_number




#print list_of_threads
    
def make_new_dictionary():
    for item in new_content:
        new_value = {}
        #print "ITEM", item
        number_of_item = new_content.index(item)
        #print number_of_item
        value = item
        value_list = [item]
        #print value_list
        #print "VALUE", value
        key = list_of_threads[number_of_item]
        post_number = list_of_post_numbers[number_of_item]
        new_value[post_number] = value
        #print key
        #print "TO DICTIONARY", new_value.values()
        new_data.setdefault(key,[]).append(new_value)
    return value_list

def thread_to_file(thread, key):
    #This doesn't work if the filename has a / in it without the if statement
    if key.find("/"):
        keysplit = key.split("/")
        key = " ".join(keysplit)
    filename = str(key)+".json"
    with open(filename, 'w') as outfile:
        json.dump(thread, outfile, encoding='utf-8')

value_list = make_new_dictionary()
for key in new_data.keys():
    thread = new_data[key]
    #print thread
    thread_to_file(thread, key)
#print dictionary_of_metadata
    
print "           " *50
    
#better_string = make_list_better([content])
print "_______________________"
print better_string
print new_content