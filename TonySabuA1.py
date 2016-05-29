""" CP5632 Assignment 1 - 2016
    Items for hire - Solution
    Tony Sabu
    11/04/2016
    github url:https: https://github.com/tonysabu33/Assignment1.git

Pseudocode:

function main()
    creating menu
    call load_items()
    display items loaded message
    display menu
    get choice
    while choice is not 'q'
        if choice is 'l'
            call list_item(items)
        else if choice is 'h'
            call hire_item(items)
        else if choice is 'r'
            call return_item(items)
        else if choice is 'a'
            call add_item(items)
        else
            display invalid choice message
        display menu
        get choice
    call save(items)
    display items saved message

function load_items()
    file=open csv file
    items=empty list
    for each line in file:
        parts=split the file
        add each part to items
    close file
    return items

function list_item(items)
    for each row in items
        if item status=in
            display items
        if item status=out
            display items with *

function hire_item(items)
    available item list=empty list
    for each row in items
        if item status=in
            display items
            add items to available item list
    if available item list==0
        display no items to hire
    else
        while True
            try
                get hire
                if hire<0
                    display enter real number
                else if hire!==available item list
                    display unavailable
                else
                    display hire message
                    remove hire from available item list
                    change status to out
                break
            exception for value error
                display invalid input

function return_item(items)
    hired item list=empty list
    for each row in items
        if item status=out
            display items
            add items to hired item list
    if available item list==0
        display no items to hire
    else
        while True
            try
                get return
                if <0
                    display enter real number
                else if return!==hired item list
                    display unavailable
                else
                    display returned message
                    remove return from hired item list
                    change status to in
                break
            exception for value error
                display invalid input

function add_item(items)
    new item list=empty list
    get name
    while name==" "
        display input cannot be blank
    add name to new item list
    get description
    while description==" "
        display input cannot be blank
    add description to new item list
    while True
        try
            get price
            if price<0
                display invalid price
            else if price==" "
                display input cannot be blank
            else
                add price to new item list
            break
        exception for value error
            display enter a valid number
    return items

function save(items)
    out_file=open csv file to write
    for i in items
        write item name
        write item description
        write item price
        write item status
    close out_file
"""


def main():
    menu = "\nMenu:\n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd an item\n(Q)uit"  # creating the menu
    print("Welcome")
    print("Written by Tony Sabu")
    items = load_items()
    print("{} items loaded from items.csv".format(len(items)))
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            list_item(items)
        elif choice == "H":
            hire_item(items)
        elif choice == "R":
            return_item(items)
        elif choice == "A":
            add_item(items)
        else:
            print("Invalid menu choice.")
        print(menu)  # printing menu
        choice = input(">>> ").upper()
    save_list(items)
    # opening the csv file to write

    print('Have a nice day :)')


def load_items():
    file = open('items.csv')  # opening the csv file

    items = []

    for line in file:
        parts = line.strip().split(",")  # splitting the csv file to parts(columns)
        parts[2] = float(parts[2])
        items.append(parts)  # adding the parts together to the items list made

    file.close()
    return items


def list_item(items):
    print('All items on file (* indicates item is currently out)')

    for number in range(len(items)):
        if items[number][3] == 'in':
            print("{} - {:15} {:35} = $ {:>6.2f}".format(number, items[number][0], '(' + items[number][1] + ')',
                                                         items[number][2]))
        else:
            print("{} - {:15} {:35} = $ {:>6.2f} *".format(number, items[number][0], '(' + items[number][1] + ')',
                                                           items[number][2]))
        number += 1


def hire_item(items):
    avl_list = []  # making a list for the available items

    for number in range(len(items)):

        if items[number][3] == 'in':  # to select the items which are available(in)
            print("{} - {:15} {:35} = $ {:>6.2f}".format(number, items[number][0], '(' + items[number][1] + ')',
                                                         items[number][2]))
            avl_list.append(number)  # appending the list of items to available item list
    if len(avl_list) == 0:
        print('no item to hire')
    else:

        valid = False
        while not valid:
            try:
                hire = int(input('Enter the number of an item to hire:'))  # getting the number of the item to hire
                if hire < 0:
                    print('Enter a real number:')
                elif hire not in avl_list:
                    print('That item is not available for hire')
                else:
                    print("{} hired for ${:2.2f}".format(items[hire][0], float(items[hire][2])))
                    avl_list.remove(hire)  # removing the item from available item's list
                    items[hire][3] = 'out'  # changing the status of item
                break

            except ValueError:
                print('Invalid input; enter a number')
                continue


def return_item(items):
    hir_list = []  # making a list for the items on hire

    for number in range(len(items)):

        if items[number][3] == 'out':  # to select the items which are on hire(out)
            print("{} - {:15} {:35} = $ {:>6}".format(number, items[number][0], '(' + items[number][1] + ')',
                                                      items[number][2]))
            hir_list.append(number)  # appending the list of items to available item list

    if len(hir_list) == 0:
        print('no items are currently on hire')
    else:

        valid = False
        while not valid:
            try:
                retn = int(input('Enter the number of an item to return:'))
                if retn < 0:
                    print('Invalid item number')
                elif retn not in hir_list:
                    print('Invalid item number')
                else:
                    print("{} returned".format(items[retn][0]))
                    hir_list.remove(retn)  # removing the item from available item's list
                    items[retn][3] = 'in'  # changing the status of item
                break

            except ValueError:
                print('Invalid input; enter a number')
                continue


def add_item(items):
    new_list = []  # making a list for the new items
    it_name = input('Item name:')
    while it_name == "":
        print('Input cannot be blank')
        it_name = input('Item name:')
    new_list.append(it_name)  # appending name of item to new item's list

    it_description = input('Description:')
    while it_description == "":
        print('Input cannot be blank')
        it_description = input('Description:')
    new_list.append(it_description)  # appending description of item to new item's list
    valid = False
    while not valid:
        try:
            it_price = float(input('Price per day:'))
            if it_price < 0:
                print('price must be >= $0\nInvalid input; enter a valid number')
            elif it_price == "":
                print('Input cannot be blank')

            else:
                new_list.append(it_price)  # appending price of item to new item's list
                new_list.append('in')

                print("{} ({}), ${} now available for hire".format(it_name, it_description, it_price))
                items.append(new_list)  # appending new item's list to items
                break
        except ValueError:
            print('Invalid input; Enter a valid number')
    return items


def save_list(items):
    out_file = open('items.csv', 'w')
    for i in range(len(items)):
        out_file.write((items[i][0] + ','))
        out_file.write((items[i][1] + ','))
        out_file.write(str(items[i][2]) + ',')
        out_file.write((items[i][3]))
        out_file.write("\n")
    out_file.close()
    print('{} items saved to item.csv'.format(len(items)))


if __name__ == '__main__':
    main()
