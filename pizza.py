# Name: Lindsay Caudle
# Prog Purpose: This program finds the cost of various pizza orders
#   S Small Pizza $9.99
#   M Medium Pizza: $12.99
#   L Large Pizza: $14.99
#   X Extra Large Pizza: $17.99
#   Sales tax rate: 5.5%

import datetime

# define tax rate and prices
SALES_TAX_RATE = .055
PR_SMALL_PIZZA = 9.99
PR_MEDIUM_PIZZA = 12.99
PR_LARGE_PIZZA = 14.99
PR_EXTRA_LARGE_PIZZA = 17.99

#define global variables
pizza_size = 0
num_pizza = 0
pizza_cost = 0
sales_tax = 0
total = 0

#define program functions
def main():
    another_order = True
    while another_order:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to place another order? (Y/N):")
        if yesno.upper() != "Y":
            another_order = False

def get_user_data():
    global pizza_size, num_pizza
    pizza_size = input("Pizza size (S,M,L,X): ")
    num_pizza = int(input("Number of pizzas: "))

def perform_calculations():
    global pizza_cost, sales_tax, total
    if pizza_size.upper() == "S":
        pizza_cost = PR_SMALL_PIZZA * num_pizza
    elif pizza_size.upper() == "M":
        pizza_cost = PR_MEDIUM_PIZZA * num_pizza
    elif pizza_size.upper() == "L":
        pizza_cost = PR_LARGE_PIZZA * num_pizza
    elif pizza_size.upper() == "X":
        pizza_cost = PR_EXTRA_LARGE_PIZZA * num_pizza
    else:
        pizza_cost = 0
    sales_tax = pizza_cost * SALES_TAX_RATE
    total = pizza_cost + sales_tax

def display_results():
    print('\n------------------------------')
    print('****** PALERMO PIZZA ******')
    print('***The best pizza in town***')
    print('------------------------------')
    print('Number of Pizzas ordered - ', num_pizza)
    print('Pizza Size               - ', pizza_size)
    print('Pizza Cost               $ ' + format(pizza_cost, '10.2f'))
    print('Sales Tax                $ ' + format(sales_tax, '10.2f'))
    print('Total                    $ ' + format(total, '10.2f'))
    print('------------------------------')
    print('**Thank you for your order, please come again!**')
    print(str(datetime.datetime.now()))

# call on main program to execute
main()
