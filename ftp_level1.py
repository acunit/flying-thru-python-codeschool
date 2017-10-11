# 1.1 - Introduction to Lists
# Lists are containers that can store anything you want
# NOTE: A Python list is called an array in other languages, like JavaScript
# empty list
empty = []
# list of numbers
nums = [10, 20, 30, 40.5]
# list of strings
words = ['cheerio', 'cheers', 'watcha', 'hiya']
# list of mixed items
anything = [10, 'hello', 'ahoy', 123.45]
# Can slive a list to get a sub-list just like you can with slicing strings
greetings = ['cheers', 'cheerio', 'watcha', 'hiya']
greetings[0]   # ==> 'cheers'
greetings[3]   # ==> 'hiya'
greetings[1:3] # ==> ['cheerio', 'watcha']

# Creating a list of British sayings
# Can do it with items already in it.
slang = ['cheerio', 'pip pip', 'smashing']
print(slang)
# Or can create an empty list
british = []
# We can add items to the end of the list with the append() funtion
slang.append('cheeky')
slang.append('yonks')
print(slang)
# Removing Elements - can remove items by using the value or index
slang = ['cheerio', 'pip pip', 'smashing', 'cheeky', 'yonks']
# removing items by value must use the remove() function
slang.remove('cheeky')
# removing items by index using the del function
del slang[3]
print(slang) # ==> ['cheerio', 'pip pip', 'smashing', 'yonks']
# we can also delete a slice or section of the list.
slang = ['cheerio', 'pip pip', 'smashing', 'yonks']
del slang[:2]
print(slang) # ==> ['smashing', 'yonks']

# Challenge 1.2 - Adding List items
# The Flying Python Circus wants to create a program to keep track of their performances and daily schedule. Let's start by creating a list to store all of the names of the performances.
performances = ['Ventriloquism', 'Amazing Acrobatics']
performances.append('Snake Charmer')
print(performances)

# Challange 1.3 - Removing List items
# Our list of performances has grown, but the Bearded Lady and the Tiniest Man have moved on, so let's remove them both from our performances list.
performances = ['Ventriloquism', 'Amazing Acrobatics', 'Snake Charmer', 'Enchanted Elephants', 'Bearded Lady', 'Tiniest Man']
performances.remove('Bearded Lady')
performances.remove('Tiniest Man')
print(performances)

# 1.5 - Introduction to Dictionaries
# What if we wanted a list to keep track of the American definitions of our British slang list?
# If we do anything to one of out lists, we have to duplicate the operations to the other list
# Example of a situation where a dictionary is useful
slang       = ['cheerio', 'pip pip', 'smashing', 'yonks', 'knackered']
translation = ['goodbye', 'goodbye', 'terrific', 'ages', 'tired']

del slang[0]
del translation[0]

print(slang)       # ==> ['pip pip', 'smashing', 'yonks', 'knackered']
print(translation) # ==> ['goodbye', 'terrific', 'ages', 'tired']

# Dictionary is similar to a list but you look values by using a key instead of an index (use curly backets instead of square)
# example of what the above would look like as a dictionary
# each item is called a key-value pair. First is Key, the : stands for assign to, then the second is the value
slang = {'cheerio':'goodbye', 'knackered':'tired', 'yonks':'ages'}
print(slang['cheerio']) # ==> 'goodbye'

# Dictionaries, like lists, can hold anything you want: numbers, strings, a mix of both, and other objects.
# Strings to strings
slang = {'cheerio':'goodbye', 'rubbish':'trash'}
# strings to numbers
menu = {'spam meal':15, 'spam with fries':10}
# Dictionary of anything
anything ={10:'hello', 2:123.45}

# Creating a Dictionary and adding values
# Create an empty dictionary:
slang = {}
# adding dictionary items: - convention goes -> dictionary[key] = value
slang['cheerio'] = 'goodbye'
slang['knackered'] = 'tired'
slang['smashing'] = 'terrific'
print(slang)
# If we wanted to update the value smashing to awesome..
slang['smashing'] = 'awesome'

# Like a list, you can use del to delete a key-value pair
slang = {'cheerio':'goodbye', 'knackered':'tired', 'smashing':'terrific'}
del slang['cheerio']
print(slang) # ==> {'knackered':'tired', 'smashing':'terrific'}

# Trying to access a key that does not exist will cause an erroy
slang['bloody'] # ==> KeyError: 'bloody'
# If you want to check if a word is in the dictionary, use get()
# Get a value that might not be there
result = slang.get('bloody')
print(result)
# If the key exists, the value will be returned
#  If the word WAS NOT in the dictionary, None will be returned
# None is a special type of value in Python that means the absence of a value
# Since None represents the absence of a value, it evaluates to False in a conditional
slang = {'cheerio':'goodbye', 'knackered':'tired'}
result = slang.get('bloody') # ==> Result equals None since no bloody key
# If exists....
if result:
    print(result)
else:
    print("Key doesn't exist")

# Using a Dictionary to Translate a Sentence
# Translate each slang word in a Sentence
slang = {'mate':'buddy', 'knackered':'tired', 'cheeky':'offensive'}
sentence = 'Sorry, my ' + 'mate' + "'s a bit " + 'cheeky' + '!'
translation = 'Sorry, my ' + slang.get('mate') + "'s a bit " + slang.get('cheeky')

print(sentence) # ==> Sorry, my mate's a bit cheeky!
print(translation) # ==> Sorry, my buddy's a bit offensive!

# Challenge 1.6 - Adding Dictionary Items
# We've started creating a dictionary to store the performances and their start times, but we need to finish adding all of the performances. Using the name of the performance as a key, set the value for that key to the time of the performance.
performances = {'Ventriloquism':'9:00am', 'Snake Charmer': '12:00pm'}
performances['Amazing Acrobatics'] = '2:00pm'
performances['Enchanted Elephants'] = '5:00pm'
print(performances)

# Challenge 1.9 - Safely get() Items
# If we tried to look up the time of the Bearded Lady show using square brackets, like this:
# print('The time of the Bearded Lady show is', performances['Bearded Lady'])
# We would get an error, causing our program to crash if it wasn't there. We can instead use get() to prevent the chance of that error.
performances = {'Ventriloquism':'9:00am',
               'Snake Charmer': '12:00pm',
               'Amazing Acrobatics': '2:00pm',
               'Bearded Lady':'5:00pm'}
showtime = performances.get('Bearded Lady')

if showtime == None:
    print("Performance doesn't exist")
else:
    print("The time of the Bearded Lady show is ", showtime)

# 1.10 - Compariing and Combining
# We can check if two lists are equal, must have same items in exact order
my_list =   [1, 2, 3, 4]
your_list = [4, 3, 2, 1]
his_list =  [1, 2, 3, 4]

print(my_list == your_list) # ==> False

print(my_list == his_list) # ==> True

# Comparing Dictionaries - Since dictionaries aren't ordered, they only need ot hav ethe same key-value paris to be equal in any order.
my_dict =   {1:1, 2:2, 3:3, 4:4}
your_dict = {4:4, 3:3, 2:2, 1:1}

print(my_dict == your_dict) # ==>True

# Lets say we have 3 separate menu lists: Breakfast, Lunch, Dinner...
 # How would we comine thse into one list?
 breakfast = ['Spam n Eggs', 'Spam n Jam', 'Spam n Ham']
 lunch     = ['SLT (Spam-Lettuce-Tomato)', 'PB&S (PB$Spam)']
 dinner    = ['Spalad', 'Spamghetti', 'Spam noodle soup']
# A list is a container of containers - menus is a list of menus
# A List of Lists - somestimes called a 2 dimensional list
menus = [ ['Spam n Eggs', 'Spam n Jam', 'Spam n Ham'],
          ['SLT (Spam-Lettuce-Tomato)', 'PB&S (PB$Spam)'],
          ['Spalad', 'Spamghetti', 'Spam noodle soup']    ]
print('Breakfast Menu:\t', menus[0])
print('Lunch Menu:\t',     menus[1])
print('Dinner Menu:\t',    menus[2])

# How would I get an element from a 2-D list?
menus = [ ['Spam n Eggs', 'Spam n Jam', 'Spam n Ham'],
          ['SLT (Spam-Lettuce-Tomato)', 'PB&S (PB$Spam)'],
          ['Spalad', 'Spamghetti', 'Spam noodle soup']    ]
print(menus[0][1]) # ==> 'Spam n Jam'
# We can make this better by not having to just know what index each menue is in. A Dictionary with keys for each menu type can do this.
menus = {'Breakfast': ['Spam n Eggs', 'Spam n Jam', 'Spam n Ham'],
         'Lunch': ['SLT (Spam-Lettuce-Tomato)', 'PB&S (PB$Spam)'],
         'Dinner': ['Spalad', 'Spamghetti', 'Spam noodle soup'] }
print('Breakfast Menu:\t', menus['Breakfast'])
print('Lunch Menu:\t', menus['Lunch'])
print('Dinner Menu:\t', menus['Dinner'])
