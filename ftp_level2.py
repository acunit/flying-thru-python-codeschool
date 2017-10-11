# 2.1 Into to Loops
# Example of loop to print out each item in a list
prices = [2.50, 3.50, 4.50]

for price in prices:
    print('Price is', price)

# Using a loop to sum our prices
# Average price
total = 0
prices = [2.50, 3.50, 4.50]

for price in prices:
    print('Price is', price)
    total = total + price
    print('total is', total)

# Averaging the prices after the loop ends
# Average price
total = 0
prices = [2.50, 3.50, 4.50]

for price in prices:
    total = total + price

average = total/len(prices)
print('avg is', average)

# Generating Raffle Tickets
# with each purchase, they get a raffle ticket, and then we draw 10 random ticket numbers at the end of the day and give out prizes
# we need to:
# 1. Generate a random ticket number
# 2. Repeat that 10 times - we can use a loop to do this!
# Generating a random ticket number
import random

r1 = random.random() # gives a random number from [0.0, 1.0]
print(r1)

r2 = random.choice([1,2,3,4,5]) # selects random number from a list
print(r2)

r3 = random.randint(1, 1000) # Gives a random number in this range
print(r3)
# In the example above, we are assuming ticket numbers are 0 - 1000, so we'll use randint()
import random
for i in range(10): # range() will create a list of numbers from 0 - 9
    ticket = random.randint(1, 1000)
    print(ticket)

# Getting more specific with range()
# we've help out circus in Orlanda every other year since 2005 until 2016
# How do we list the years?
for i in range(2005, 2016, 2): # range(start, stop, step)
    print(i)

# Challenge 2.2 - for Loops With a List
# We want to print a big vertical Welcome sign for our circus, and to do that we want to print each letter of 'Welcome!' on a separate line. We can do this with a for loop — for each letter in our word, we'll print it.
word = 'Welcome!'
for letter in word:
    print(letter)

# Challenge 2.6 - Looping With range()
# Let's help the fortune-teller robot generate random lotto ticket suggestions for its customers. We'll use a for loop to pick five random numbers between 1 and 53.
for i in range(5):
    print(random.randint(1, 53))

# 2.7 - More For Loops in Action
# For each British slang word, let's create a menu item made with Spam.
slang = ['Knackered', 'Pip pip', 'Squidgy', 'Smashing']
menu = []

for word in slang:
    menu.append(word + ' Spam')

print(menu) # ==> ['Knackered Spam', 'Pip pip Spam', 'Squidgy Spam', 'Smashing Spam']

# For each menue item, lets also assign a price

menu = ['Knackered Spam', 'Pip pip Spam', 'Squidgy Spam', 'Smashing Spam']
# Let's store the menu items with their prices in a dictionary; keys will be item name, values will be the price.
menu_prices = {}
price = 0.50
for item in menu:
    menu_prices[item] = price
    price = price + 1

print(menu_prices) # ==> {'Knackered Spam': 0.5, 'Pip pip Spam': 1.5, 'Squidgy Spam': 2.5, 'Smashing Spam': 3.5}

# Printing Our Menu items, want to price the key and value
menu_prices = {'Knackered Spam': 0.5, 'Pip pip Spam': 1.5, 'Squidgy Spam': 2.5, 'Smashing Spam': 3.5}

for name, price in menu_prices.items(): # dict_name.items() gives us a list of keys and values inside a dictionary
    print(name, ': $', format(price, '.2f'), sep='') # sep= in the print function can override the default space that is used to separate each item in the print() function.
    # We can format our price float to two decimals using format(); .2f means f for float and 2 for decimal places.

# NOTE: To get a list of keys in a dictionary, use dict_name.keys() and to get a list of the values, use dict_name.values()

# Challenge 2.8 - for Loops With Dictionaries
# We want to print out a schedule of our circus' performances. To do this, we can take our dictionary of performances and print out each item on a separate line using a for loop.
performances = {'Ventriloquism':'9:00am',
                'Snake Charmer': '12:00pm',
                'Amazing Acrobatics': '2:00pm',
                'Enchanted Elephants':'5:00pm'}
for name, showtime in performances.items():
    print(name, ': ', showtime, sep='')

# 2.9 - While Loops
# We want to let customers order and add as many items as they want. A for loop wouldn't be good for this because we don't know haow many times to loop...
# For loops let you loop a certain number of times.
# A while loop continue looping while a condition is true.
# Simple while Loop example
x = 1
while x != 3: # stopes when x is equal to 3
    print('x is', x)
    x = x + 1

# Let's create our ordering interface using while loops
# menu = {'Knackered Spam':'Knackered Spam', 'Pip pip Spam':'Pip pip Spam', 'Squidgy Spam':'Squidgy Spam', 'Smashing Spam':'Smashing Spam'}
# orders = []
# order = input("What would you like to order? (Q to Quit)")
# while (order.upper() != 'Q'):
#     # Find the order and add it to the list if it exists
#     found = menu.get(order) # Checks to see if the order is on menu
#     if found:
#         orders.append(order)
#     else:
#         print("Menu item doesn't exist")
#
#     # See if the customer wants to order anything else
#     order = input("Anything else? (Q to Quit)")
#
# print(orders)

# Another way to break out of the loop
# a break statement will exit the loop immediately and continue running the program. It's just a different way to doing what is above.
# menu = {'Knackered Spam':'Knackered Spam', 'Pip pip Spam':'Pip pip Spam', 'Squidgy Spam':'Squidgy Spam', 'Smashing Spam':'Smashing Spam'}
# orders = []
# order = input("What would you like to order? (Q to Quit)")
#
# while (True):
#     if order.upper() == 'Q':
#         break
#     # Find the order and add it to the list if it exists
#     found = menu.get(order) # Checks to see if the order is on menu
#     if found:
#         orders.append(order)
#     else:
#         print("Menu item doesn't exist")
#
#     # See if the customer wants to order anything else
#     order = input("Anything else? (Q to Quit)")
#
# print(orders)

# # Pretend we ran out of Cheeky Spam (and example of an infinite loop creation. THIS IS VERY BAD!!!)
# menu = {'Knackered Spam':'Knackered Spam', 'Pip pip Spam':'Pip pip Spam', 'Squidgy Spam':'Squidgy Spam', 'Smashing Spam':'Smashing Spam'}
# orders = []
# order = input("What would you like to order? (Q to Quit)")
#
# while (True):
#     # NOTE below statement creates an infinite loop!
#     if order == 'Cheeky Spam':
#         print("Sorry, we're all out of that!")
#         continue
#     if order.upper() == 'Q':
#         break
#     # Find the order and add it to the list if it exists
#     found = menu.get(order) # Checks to see if the order is on menu
#     if found:
#         orders.append(order)
#     else:
#         print("Menu item doesn't exist")
#
#     # See if the customer wants to order anything else
#     order = input("Anything else? (Q to Quit)")
#
# print(orders)

# Fixing our infinite Loop
# We need to get the customer's order at the top of our loop now so they can change their order.
menu = {'Knackered Spam':'Knackered Spam', 'Pip pip Spam':'Pip pip Spam', 'Squidgy Spam':'Squidgy Spam', 'Smashing Spam':'Smashing Spam'}
orders = []

while (True):
    # See if they customer wants to order anything else
    order = input("Can I take your order? (Q to Quit)")

    if order == 'Cheeky Spam':
        print("Sorry, we're all out of that!")
        continue
    if order.upper() == 'Q':
        break

    # Find the order and add it to the list if it exists
    found = menu.get(order) # Checks to see if the order is on menu
    if found:
        orders.append(order)
    else:
        print("Menu item doesn't exist")

print('You ordered:', orders)

# Challenge 2.10 - Guess the Number Game
# We want to create a "guess the number" game for our fortune-teller robot. If you guess the random number between 1 and 10, you win a crystal ball!
# There is some code that's been written for us — getting the random number the user needs to guess, and printing 'You win!' if they win. We need to write the code to get the user's guess and compare it to num.
import random

num = random.randint(1,10)

# Add your code here
guess = int(input('Guess a number between 1 and 10'))

while (guess != num):
    guess = int(input('Guess again'))

print('You win!')

# Challenge 2.11 - Guess the Number Game (improved)
# Now our fortune-teller robot has a "guess the number" game — if you guess the random number between 1 and 10, you win a crystal ball! But the game lets the user guess 10 times, so they always win… #fail. Let's fix the game so they can only guess three times.
import random

num = random.randint(1,10)

guess = int(input('Guess a number between 1 and 10'))
times = 1

while guess != num:
    guess = int(input('Guess again'))
    times = times + 1
    if times == 3:
        break

if guess == num:
    print('You win!')
else:
    print('You lose! The number was ', num)
