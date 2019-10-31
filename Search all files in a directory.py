# Performs a RegEx search for a string inside a directory (define the file extention required)

from os import listdir
import re

list_file = []
list_directory = []

def sorting_function(f):
    return len(f)

directory = 'C:\\Users\\Files'
search_string = r'\s+search_for_this\s+' # RegEx - more flexible than a string match

for d in sorted(listdir(directory), key=sorting_function):
    if d.endswith('.txt') or d.endswith('.ini'):
        list_file.append(d)

print('File summary:\n==================')
for f in list_file:
    file = open(directory+f, 'r')
    try:
    	match = re.findall(search_string, file.read(), re.DOTALL|re.MULTILINE)
    	if match:
    		print(f)
    except:
    	pass

    file.close()

print('\nLines where found:\n==================')
for f in sorted(list_file, key=sorting_function):
    file = open(directory+f)
    for l in enumerate(file):
    	try:
    		match = re.search(search_string, l[1], flags=0).group().strip()
    		if match:
    			print(f + '\t' + str(l[0]) + '\t' + l[1].replace('\n', ''))
    	except:
         	pass

    file.close()

   
