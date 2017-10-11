# Level 3 - Fuctions

# 3.1 How to Create Functions
# Problem: We're repeating a lot of code

# We've got this code to get average price
# Average price
total = 0
prices = [2.50, 3, 4.50, 5]

for price in prices:
    total = total + price

average = total/len(prices)

# This code that gets the average daily customers
total = 0
customers = [29, 21, 55, 5, 10, 14, 12]

for cust in customers:
    total = total + cust

average = total/len(customers)

# Now we want to write code to calc avaerage daily sales...
# Wouldn't it be nice to have one peice of code to average anything we ask it to?

# Functions are like mini programs that allow us to perform a specific task
# We've been using functions all along like print() and range()

# Making out own functions
# Need to define 3 things.
# 1 What is the function name?
# 2 What data do we send into the function?
# 3 What data comes out of the function?

def average(prices):
    total = 0

    for price in prices:
        total = total + price

    avg = total/len(prices)
    return avg # returning data is optional.

# Calling the average function
# functions don't run until you call them.
numbers = [1,2,3,4,5]
my_average = average(numbers)
print(my_average)

# Generalizing Our average() Function - better readability
def average(numbers):
    total = 0

    for num in numbers:
        total = total + num

    avg = total/len(numbers)
    return avg

daily_sales = [10,14,8]
result = average(daily_sales)
print(result)

# Use our function on prices
prices = [2.50, 3, 4.50, 5]
result = average(prices)
print(result)


# Challenge 3.3 - A Function for Lottery Numbers
# The fortune-teller robot wants us to create a function for generating lottery ticket numbers. We'll take the code we already created in Level 2, but instead of printing out the numbers one by one, our function will return a list of the numbers.
import random

def lotto_numbers():
    lotto_nums = []
    for i in range(5):
        lotto_nums.append(random.randint(1, 53))

    return(lotto_nums)

# Challenge 3.4 - Calling Our Function
# Let's call the lotto_numbers() function we just created.
import random

def lotto_numbers():
    lotto_nums = []
    for i in range(5):
        lotto_nums.append(random.randint(1, 53))

    return(lotto_nums)

numbers = lotto_numbers()
print(numbers)

# 3.5 main() and Scope
# A best practice is to organize our main program code into a function called... main()
# BEFORE
def average(numbers):
    total = 0
    for num in numbers:
        total = total + num

    avg = total/len(numbers)
    return avg

# main
prices = [29, 21, 55, 10]

result = average(prices)

print(result)

# AFTER
def average(numbers):
    total = 0
    for num in numbers:
        total = total + num

    avg = total/len(numbers)
    return avg

def main():
    prices = [29, 21, 55, 10]
    result = average(prices)
    print(total) # This would result in an error, since total is defined in the average function, not the main() (local scope)
    print(result)

order_goal = 25 # This is global scope, so can be accessed inside average() and main()
main() # All of the execution starts here!
order_goal = 25 # If order_goal is declared after we run main() it wont be accessible within the main() function items.


# Challenge 3.6 - Adding main()
# Now that we have a function to create lottery numbers and we're calling it successfully, we'll want to organize our code better. We've created a main() function at the bottom of our script, and now we need to call lotto_numbers() from it.
import random

def lotto_numbers():
    lotto_nums = []
    for i in range(5):
        lotto_nums.append(random.randint(1, 53))

    return lotto_nums

def main():
    numbers = lotto_numbers()
    print(numbers)

main()

# 3.9 - Making More Functions
# When to Create Functions?
# Functions should be used for any chunk of code that has a specific purpose. For instance, here are all the things we want to implement in our Food Truck Order System:
# 1. Print the menu
# 2. Take an order
# 3. Calculate the total bill
# The above tasks are all pretty self contained, so it makes sense that we would create separate functions for them.

# Writing a Funtion to Print Our Menu
menu = {'Knackered Spam': 0.5, 'Pip pip Spam': 1.5, 'Squidgy Spam': 2.5, 'Smashing Spam': 3.5}

# 1. Print the menu
def print_menu(menu):
    for name, price in menu.items():
        print(name, ': $', format(price, '.2f'), sep='')

# 2. Take an order
def get_order(menu):
    orders = []
    order = input("What would you like to order? (Q to Quit)")

    while (order.upper() != 'Q'):
        # find the order
        found = menu.get(order)
        if found:
            orders.append(order)
        else:
            print("Menu item doesn't exist")

        order = input("Anything else? (Q to Quit)")

    return orders

# 3. Calculate the total bill
def bill_total(orders, menu):
    total = 0

    for order in orders:
        total += menu[order]

    return total

def main():
    menu = {'Knackered Spam': 0.5, 'Pip pip Spam': 1.5, 'Squidgy Spam': 2.5, 'Smashing Spam': 3.5}
    print_menu(menu)
    orders = get_order(menu)
    total = bill_total(orders, menu)
    print("You ordered:", orders, "Your total is: $", format(total, '.2f'), sep='')

main()

# Challenge 3.10 - Guess the Number Function
# The fortune-teller robot wants to be able to easily generate lotto numbers and play the "guess the number" game. We'll improve the robot's program by moving the code we wrote previously for the "guess the number" game into its own function.
import random

def guessing_game():
    num = random.randint(1, 10)

    guess = int(input('Guess a number between 1 and 10'))
    times = 1

    while guess != num:
        guess = int(input('Guess again'))
        times += 1
        if times == 3:
            break

    if guess == num:
    	  print('You win!')
    else:
        print('You lose! The number was', num)


def lotto_numbers():
    lotto_nums = []
    for i in range(5):
        lotto_nums.append(random.randint(1, 53))

    return lotto_nums

def main():
    numbers = lotto_numbers()
    print(numbers)
    guessing_game()

main()

# Challenge 3.11 - User's Choice
# We want the fortune-teller robot to be able to ask the user if they want to play the guess the number game or if they want lottery numbers.
import random

def guessing_game():
    num = random.randint(1, 10)

    guess = int(input('Guess a number between 1 and 10'))
    times = 1

    while guess != num:
        guess = int(input('Guess again'))
        times += 1
        if times == 3:
            break

    if guess == num:
        print('You win!')
    else:
        print('You lose! The number was', num)


def lotto_numbers():
    lotto_nums = []
    for i in range(5):
        lotto_nums.append(random.randint(1, 53))

    return lotto_nums

def main():
    answer = input('Do you want to get lottery numbers (1) or play the game (2) or quit (Q)?')

    if answer == '1':
        numbers = lotto_numbers()
        print(numbers)
    elif answer == '2':
        guessing_game()
    else:
        print('Toodles!')

main()
