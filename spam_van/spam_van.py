import orders

def main():
    menu = {'Knackered Spam': 0.5, 'Pip pip Spam': 1.5, 'Squidgy Spam': 2.5, 'Smashing Spam': 3.5}
    orders.print_menu(menu)
    order = orders.get_order(menu)
    total = orders.total_bill(order, menu)
    print("You ordered:", order, "Your total is: $", format(total, '.2f'), sep='')

main()
