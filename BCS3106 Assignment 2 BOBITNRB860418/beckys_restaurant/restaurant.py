from os import system, startfile
from datetime import datetime


title = ("BECKY'S RESTAURANT ORDERING SYSTEM")  # Title of the system


def newLine():                                  # Displays a blank line on the terminal
    print()


def clearScreen():                              # Clears the terminal to display new information
    system('cls')
    newLine()


def pressEnter():                               # Waits for the user to press enter
    newLine()                                   # before moving to the next operation
    input('Press "ENTER" key to continue...')
    newLine()


def readFile(filename):                         #
    opened_file = open(filename, 'r')           # Opens a text file,
    lines_read = opened_file.readlines()        # reads its lines
    opened_file.close()                         # and returns it as a string
    return lines_read                           #


def writeToFile(filename, information):         #
    opened_file = open(filename, 'w')           # Writes lines passed
    opened_file.writelines(information)         # as a string to a text file
    opened_file.close()                         #


def mainMenu():                                 # Displays main menu on the terminal
    print(title)
    print('-'*len(title))
    print('>> Place Order (P)')
    print('>> Cancel Last Order (C)')
    print('>> Exit (E)')
    newLine()


def displayMenu(menu_list, menu_number = 0):    # Dislpays the menu on the terminal
    clearScreen()
    print(title)
    print('-'*len(title))
    print('NO.\tITEM\t\tTYPE\t\tPRICE')
    print('---\t----\t\t----\t\t-----')
    menu = readFile('menu.txt')                 # Reads menu file
    for line in menu:
        if line[-1] == '\n':                    # Checks for the new line character removes it
            menu_item = line[:-1].split(' ')    # to avoid blank lines on the terminal then
            menu_list.append(menu_item)         # adds the line to the menu list
        else:
            menu_item = line.split(' ')         # Adds lines without the new line character
            menu_list.append(menu_item)         # to the menu list

    for menu_item in menu_list:
        menu_number += 1
        print(f"{menu_number}\t{menu_item[0]}\t\t{menu_item[1]}\t\t{menu_item[2]}")
    return menu_number                          # Returns the number of items on the menu list


def displayReceipt(customer_order, total, cash_tendered):       # Displays the receipt after customer
    print("xxxxx ---------- xxxxx\n")                           # has paid for the ordered items
    print("BECKY'S RESTAURANT")
    print("----------------------")
    print("ITEM\t\tPRICE")
    print("----\t\t-----")
    for order in customer_order:
        print(f'{order[0]}\t\t{order[2]}')
    print('-----\t\t-----')
    print(f'TOTAL: \t\t{total}')
    print("-----------------------")
    print(f"Cash Tendered:\t{cash_tendered}")
    print(f"CHANGE:\t\t{cash_tendered - total}")
    print("-----------------------")
    print(f"Date: {datetime.now().strftime('%d, %h %Y')}")      # Gets the date and formats it
    print(f"Time: {datetime.now().strftime('%H:%M:%S')}")       # Gets the time and formats it
    print("-----------------------")
    print("Thank You.\nCome again.")
    print("\nxxxxx ---------- xxxxx")


def printReceipt(customer_order, total, cash_tendered):         # Handles printing of the receipt
    line_to_write = ''
    lines = []
    lines.append("xxxxx ---------- xxxxx\n\n")
    lines.append("BECKY'S RESTAURANT\n")
    lines.append("----------------------\n")
    lines.append("ITEM\t\tPRICE\n")
    lines.append("----\t\t-----\n")
    for order in customer_order:
        lines.append(f'{order[0]}\t\t{order[2]}\n')
    lines.append('-----\t\t-----\n')
    lines.append(f'TOTAL: \t\t{total}\n')
    lines.append("-----------------------\n")
    lines.append(f"Cash Tendered:\t{cash_tendered}\n")
    lines.append(f"CHANGE:\t\t{cash_tendered - total}\n")
    lines.append("-----------------------\n")
    lines.append(f"Date: : {datetime.now().strftime('%d, %h %Y')}\n")
    lines.append(f"Time: {datetime.now().strftime('%H:%M:%S')}\n")
    lines.append("-----------------------\n")
    lines.append("Thank You.\nCome again.\n")
    lines.append("\nxxxxx ---------- xxxxx")

    for line in lines:
        line_to_write += str(line)

    writeToFile('current_receipt.txt', line_to_write)                       # Saves current receipt to file
    startfile('current_receipt.txt', 'print')                               # Opens receipt file and prints it


def placeOrder(customer_order = [], total = 0, cash_tendered = 0):          # Places and order
    while True:
        menu_list = []
        menu_number = displayMenu(menu_list)                                # Displays menu
        
        newLine()
        user_input = int(input('Enter menu no.: ').strip())                 # Selects an item from the menu
        while user_input > menu_number:
            print('INVALID MENU ITEM!\nPLEASE TRY AGAIN!\n')
            user_input = int(input('Enter menu no.: ').strip())

        customer_order.append(menu_list[(user_input)-1])

        newLine()
        user_input = input('Add another item?(Y/N): ').upper().strip()
        while user_input not in ['Y', 'N']:
            print('ENTER A VALID INPUT!\n')
            user_input = input('Add another item?(Y/N): ').upper().strip()

        if user_input == 'N':
            break
        elif user_input == 'Y':
            continue

    clearScreen()
    print('ITEMS ORDERED')                                              #
    print('-------------')                                              #
    print('ITEM\t\tPRICE')                                              #
    print('----\t\t-----')                                              # Displays items ordered
    for order in customer_order:                                        #
        print(f'{order[0]}\t\t{order[2]}')                              #
        total += int(order[2])                                          #
    print('------\t\t-----')
    print(f'TOTAL: \t\t{total}')

    newLine()
    user_input = input('Process payment?(Y/N): ').upper().strip()       # Processes payment
    while user_input not in ['Y', 'N']:
        print('ENTER A VALID INPUT!\n')
        user_input = input('Process payment?(Y/N): ').upper().strip()
    if user_input == 'Y':
        while True:
            newLine()
            cash_tendered = int(input('Enter amount tendered: '))
            if cash_tendered < total:
                print('\nCASH TENDERED CANNOT BE LESS THAN THE TOTAL!')
            else:
                break
        change = cash_tendered - total
        newLine()
        print(f'Payment Processed. CHANGE is {change}.')

        pressEnter()
        clearScreen()

        displayReceipt(customer_order, total, cash_tendered)            # Displays receipt
        newLine()
        user_input = input("Print receipt? (Y/N): ").upper().strip()
        while user_input not in ['Y', 'N']:
            print('ENTER A VALID INPUT!\n')
            user_input = input("Print receipt? (Y/N): ").upper().strip()
        if user_input == "Y":
            printReceipt(customer_order, total, cash_tendered)          # Prints receipt
            pressEnter()
        elif user_input == "N":
            pressEnter()

        clearScreen()
        order_schedule = []
        for order in customer_order:
            if order[1] == 'starter':                       #
                order_schedule.insert(0, order)             # Schedule orders so that starters are
            elif order[1] == 'main':                        # served first
                order_schedule.insert(-1, order)            #
        order_no = 0
        print('CUSTOMER ORDER')
        print('--------------')
        for order in order_schedule:
            order_no += 1
            print(f'{order_no}. {order[0].title()}')        # Displays the schedule
        
        pressEnter()

        line_to_write = ''
        lines = []
        order_no = 0
        lines.append('CUSTOMER ORDER\n')
        lines.append('--------------\n')
        for order in order_schedule:
            order_no += 1
            lines.append(f'{order_no}. {order[0].title()}\n')
        for line in lines:
            line_to_write += str(line)
        
        writeToFile('current_order.txt', line_to_write)
        startfile('current_order.txt', 'print')             # Prints the scheduled order

        record = ''
        for order in customer_order:
            for item in order:
                if order[-1] == item:
                    record = record + item
                else:
                    record = record + item + ' '
            if customer_order[-1] == order:
                pass
            else:
                record = record + ','
        record = record + '\n'

        lines = readFile('orders.txt')
        lines.append(record)
        writeToFile('orders.txt', lines)                    # Records current order to file

        customer_order.clear()

    elif user_input == "N":                                 # Cancels current order
        print("\nOrder cancelled...")
        customer_order.clear()
        pressEnter()


def cancelLastOrder():                                      # Cancels an already paid for order
    clearScreen()
    lines = readFile('orders.txt')
    last_order = lines[-1]
    lines = lines[:-1]
    writeToFile('orders.txt', lines)
    print(f'\nOrder: {last_order}\nDELETED!')
    pressEnter()


while True:                                                 # Main program loop
    clearScreen()
    mainMenu()
    user_input = input('Input: ').upper().strip()           # Gets user input after displaying the main menu
    if user_input == 'P':
        placeOrder()                                        # Initiates placing an order
    elif user_input == 'C':
        cancelLastOrder()                                   # Cancels paid for order
    elif user_input == 'E':
        clearScreen()                                       # Exits the loop hence the system
        break
    else:
        newLine()
        print('PLEASE ENTER A VALID INPUT!')
        pressEnter()

newLine()
print('EXITING SYSEM!')
pressEnter()
