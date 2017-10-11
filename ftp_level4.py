# Level 4 - Reading and Writing Files

# 4.1 - Writing Files
# PROBLEM: Our orders disapper when we quit
# Let's say we have a short program that gets a dictionary of orders from a customer. As soon as the program ends, the dictionary is not in memory anymore...

# How to Write to a File
# Here are the steps to write to a file.

# 1. Open the file with the opne() function. first parameter is the file name and the second is the Mode ('w' - Write (will overwrite the existing content in the file), 'r' - Read, and 'a' - Append)
# sales_log = open('spam_orders.txt', 'w')
#
# # 2. Write to the file
# sales_log.write('The Spam Van\n')
# sales_log.write('Sales Log')
#
# # 3. Close the file
# sales_log.close()

# We Need to Build a Customer Sales Log
# After we get a customer's order, it would be great if we could record each sale to a sales.txt file.
# Customer 1
# order = {'Cheeky Spam': 1.0, 'Chips Spam': 4.0}
# # Customer 2
# order = {'Knackered Spam': 1.0}
# # Customer 3
# order = {'Cheerio Spam': 1.0, 'Smashing Spam': 3.0}

# Steps to Write to Our Sales Log
# order = {'Cheeky Spam': 1.0, 'Chips Spam': 4.0}

def write_sales_log(order):
    # open the file in mode 'a' for append
    file = open('sales.txt', 'a')

    # write each item to the file
    # write the total to the file
    total = 0
    for item, price in order.items():
        file.write(item + ' ' + format(price, '.2f') + '\n')
        total += price

    file.write('total = ' + format(total, '.2f') + '\n\n')
    # close the file
    file.close()

def main():
    order = {'Cheeky Spam': 1.0, 'Chips Spam': 4.0}
    write_sales_log(order)
    order = {'Cheerio Spam': 1.0, 'Smashing Spam': 3.0}
    write_sales_log(order)

# main() remember to call this in order for it to happen.

# Challenge 4.3 - Writing the Circus Schedule
# Whenever we update the schedule we'll write it to a file so that other programs, like the circus website, can use it. We want to take our performances dictionary and write each item into a schedule.txt file so the file looks like this:
#  Ventriloquism - 9:00am
#  Snake Charmer - 12:00pm
#  Amazing Acrobatics - 2:00pm
#  Enchanted Elephants - 5:00pm
performances = {'Ventriloquism':       '9:00am',
                'Snake Charmer':       '12:00pm',
                'Amazing Acrobatics':  '2:00pm',
                'Enchanted Elephants': '5:00pm'}

schedule_file = open('schedule.txt', 'w')

for key, val in performances.items():
    schedule_file.write(key + ' - ' + val + '\n')

schedule_file.close()

# 4.4 - Reading Files
# Spam Van has a value menu
# Every day, the boss sends us a file of dollar menu items. We want to read this file into the list so our program can use it.
# Reading the Entire Contents of a File
# Steps are similar to write.
# file_name.read() will return a strong containing the entire contents of the file
# 1. First open the file.
# dollar_spam = open('dollar_menu.txt', 'r')
# # 2. Read from the file
# print(dollar_spam.read())
# # 3. Close the file
# dollar_spam.close()
#
# # Reading an Individual Line From a File
# # file_name.readline() will return a string for the next single line in teh file.
# def read_dollar_menu():
#     dollar_spam = open('dollar_menu.txt', 'r')
#     print('1st line:', dollar_spam.readline())
#     print('2nd line:', dollar_spam.readline())
#     dollar_spam.close()
#
# # What does the above example better is to read each of the individual lines using a loop so it doesn't matter how many lines there are.
# def read_dollar_menu():
#     dollar_spam = open('dollar_menu.txt', 'r')
#
#     for line in dollar_spam:
#         print(line)
#
#     dollar_spam.close()

# Okay, now that we can print each line, lets try organizing them into a list called Dollar Menu
def read_dollar_menu():
    dollar_spam = open('dollar_menu.txt', 'r')

    dollar_menu = []
    for line in dollar_spam:
        line = line.strip() # str.strip() removes any leading or trailing whitespace.
        dollar_menu.append(line)

    print(dollar_menu)
    dollar_spam.close()

# Challenge 4.5 - Reading schedule.txt
# We'll also need to be able to read our schedule file back into a dictionary. Right now our schedule.txt file looks like this:
# Ventriloquism - 9:00am
# Snake Charmer - 12:00pm
# Amazing Acrobatics - 2:00pm
# Enchanted Elephants - 5:00pm
schedule_file = open('schedule.txt', 'r')
for line in schedule_file:
    print(line)
schedule_file.close()

# Challenge 4.6 - Splitting a String
# Now we'll use some Python tricks we haven't seen before. The performance is separated from the time by a dash ' - '. We can divide that string by using line.split(' - ') and this will return two separate things: the show and the time.
schedule_file = open('schedule.txt', 'r')
for line in schedule_file:
    (show, time) = line.split(' - ')
    print(show, time)
schedule_file.close()

# Challenge 4.7 - Reading into a Dictionary
# Now that we have the performance and time from each line in our file, let's save them into a dictionary.
performances = {}

schedule_file = open('schedule.txt', 'r')

for line in schedule_file:
    (show, time) = line.split(' - ')
    print(show, time)
    performances[show] = time.strip()

schedule_file.close()
print(performances)

# 4.8 - Exceptions
# PROBLEM: The Program Crashes When an Error Happens
# What happens if we try to open a file that doesn't exist?
# my_file = open('name.txt', 'r') ==> FileNotFoundError
# This will cause our program to crash
# It would be great if we could recover and continue our program even if we get an error
# Try Except allows us to do this.

# Using Try, Except to Recover From Errors
# Try, Except blocks catch errors so that we can avoid a program crash.
try: # Like saying, 'try this' and if you get an error...
    file = open('sales.txt', 'r')
    print(file.read())
except: # Go here and print this error message
    print("File doesn't exist")
# And then continue with the program

# Types of Exceptions
# Python has 60-plus types of exceptions. Here are some of the ones we've seen before:
# FileNotFoundError - File doesn't exist
# IndexError - Index out of bounds
# KeyError - Key doesn't exist
# NameError - Variable name doesn't exist in local or global scope
# ValueError - Value is the wrong type

# We can also use try, except in other situations that might have unexpected problems... like casting user input to a number.
price = input("Enter the price: ")

try:
    price = float(price)
    print('Price =', price)
except ValueError as err: # create variable 'err' to hold error msg
    print(err)

# Challenge 4.9 - Try, Except, Succeed
# If for some reason we try to read our schedule.txt file and it doesn't exist, our program will crash. Let's fix this by adding exception handling to our schedule reader program.
performances = {}

try:
    schedule_file = open('schedule.txt', 'r')
except FileNotFoundError as err:
    print(err)

for line in schedule_file:
    (show, time) = line.split(' - ')
    performances[show] = time

schedule_file.close()
print(performances)
