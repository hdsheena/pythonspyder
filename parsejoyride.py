import json
from text_unidecode import unidecode 

file = open('joyride2.json', 'rb')
data = json.loads(file.read())

just_data = data['data']

new_data = {}

def make_list_better(list_item):
    """
    The unicode stuff makes me crazy. This fixes it
    """
    print list_item[0][0]
    better = unidecode(list_item)
    print list_item[0]
    print better
    return better
    
    


dates = []
content = []
def create_lists_of_content_and_meta(just_data):
    """This takes the data section from importio's output file, and
    makes it into some nice useable lists. They're in order, and this is 
    important later.
    """
    for item in just_data:
        if "test" in item.keys():
            to_dates = item['test']
            #print to_dates[0]
            dates.append(to_dates[0])
        else:
            to_content = item['date']
        
            content.append(to_content[0])

new_content = []

def make_content_strings_useable(content_list):
        for item in content_list:
            new_item = make_list_better(item)
            new_content.append(new_item)
    
dictionary_of_metadata = {}
list_of_threads = []
list_of_post_numbers = []

def make_nice_lists(dates_list):
   """
   make dates string into time stamp and topic heading
   """
   for item in dates_list:
        string = item
        date_string = string.replace('#', 'to:')
        split_string = date_string.split('to:')
        name_of_thread = split_string[1][1:-1]
        post_number = split_string[2]
        list_of_threads.append(name_of_thread)
        list_of_post_numbers.append(post_number)
        dictionary_of_metadata[name_of_thread] = post_number




def make_new_dictionary(new_content, new_data):
    for item in new_content:
        new_value = {}
        number_of_item = new_content.index(item)
        key = list_of_threads[number_of_item]
        post_number = list_of_post_numbers[number_of_item]
        new_value[post_number] = item
        new_data.setdefault(key,[]).append(new_value)
    

def thread_to_file(thread, key):
    #This doesn't work if the filename has a / in it without the if statement
    if key.find("/"):
        keysplit = key.split("/")
        key = " ".join(keysplit)
    filename = str(key)+".json"
    with open(filename, 'w') as outfile:
        json.dump(thread, outfile, encoding='utf-8')

def dictionary_to_files(new_data):
    for key in new_data.keys():
        thread = new_data[key]
        thread_to_file(thread, key)
    
    
#Calling all my functions to make things happen
    
create_lists_of_content_and_meta(just_data)
make_content_strings_useable(content)
make_nice_lists(dates)
make_new_dictionary(new_content, new_data)
dictionary_to_files(new_data)

