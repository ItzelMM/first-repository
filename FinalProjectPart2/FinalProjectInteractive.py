# Itzel Munoz Monroy PSID: 1888446
# Importing the Items class and function from my other files
import FinalProjectClass2
from FinalProjectFunction import *
manufacturers = open("ManufacturerList.csv", "r")
rows_m = manufacturers.readlines()
prices = open("PriceList.csv", "r")
rows_p = prices.readlines()
dates = open("ServiceDatesList.csv", "r")
rows_d = dates.readlines()

# Creating empty lists that will be used later
good_list = []  # This list will contain all the items that aren't damaged or past their service date
damages = []   # This list will contain all the items that are damaged
names = []     # This list will contain all the manufacturer names
dates_list = []  # This list will contain all the items past their service date
types_list = []  # This list will contain all the types of items
possible = []   # This list will be filled with the items that match the user's input
other_type = []   # This list will be filled with item suggestions based on the type of item
other_name = []   # This list will be filled with item suggestions based on the manufacturer name


# This loop goes through the input files and
# organizes items in the appropriate lists
# using the Items class' attributes and methods
for row in rows_m:
    item = FinalProjectClass2.Items()
    columns = row.split(",")
    item.item_id = str(columns[0])
    item.item_name = (str(columns[1])).lower()
    names.append(item.item_name)
    item.item_type = (str(columns[2])).lower()
    types_list.append(item.item_type)
    item.item_damage = str(columns[3])
    for row_p in rows_p:
        columns_p = row_p.split(",")
        if columns_p[0] == item.item_id:
            item.item_price = str(columns_p[1]).strip('\n')
    for row_d in rows_d:
        columns_d = row_d.split(",")
        if columns_d[0] == item.item_id:
            item.item_date = str(columns_d[1]).strip('\n')
    item.add_date(dates_list)
    item.add_damage(damages)
    item.good_items(good_list, dates_list, damages)

response = ""
print("Itzel's Electronic Shop Production Information")
# Printing instructions for the user
print("Please enter the name of the manufacturer and type of product\n"
      "you are interested in; or press q to exit.")

# Creating a while loop that will keep prompting the user until they enter q
while response != "q":
    other_name = []  # This empties the other_name list everytime a new prompt is entered
    other_type = []  # This empties the other_type list everytime a new prompt is entered
    possible = []   # This empties the possible list everytime a new prompt is entered
    check = -1
    check2 = -1
    response = input()
    response = response.lower()   # This converts the user input to all lowercase,
    # this way the program will still be able to find the desired product regardless
    # if the user capitalizes or doesn't capitalize their input.

    # This for loop checks if the user input is in our manufacturer name's list
    for name in names:
        if response.find(name) != -1:
            check = 0
            break

    # This for loop checks if the user input is in our items type list
    for i_type in types_list:
        if response.find(i_type) != -1:
            check2 = 0
            break

    # If the user input is doesn't include a name or type that is on our lists,
    # and it's not "q", then print "No such item in inventory".
    if (check == -1 or check2 == -1) and response != "q":
        print("No such item in inventory.")

    # Else if the user input is on our name and type lists, another for loop goes
    # through the good_list (which doesn't contains damaged or past date items).
    elif response != "q":
        for item in good_list:
            # If the both the user manufacturer name and item type are in the good_list
            # then that item is added to the possible list.
            if (item[1] in response) and (item[2] in response):
                possible.append(item)
            # Adds items with same manufacturer name as input to other_name list
            if item[1] in response:
                other_name.append(item)
            # Adds items with same item type as input to other_type list
            if (item[2] in response) and (item[1] not in response):
                other_type.append(item)

        if not possible:
            # If there wasn't an exact match of the user's manufacturer name and item type
            # (meaning the possible list would be empty), then this statement is printed.
            print("We do not have such item in inventory.")
            if len(other_name) != 0:
                print("You may like to consider other items from said manufacturer.")
                answer(other_name, 1)
            if len(other_type) != 0:
                print("You may like to consider similar items from other manufacturers.")
                answer(other_type, 1)
        else:
            # If there was an exact match of the user's manufacturer name and item type
            # then that match's information is printed.
            print("This is your item:", end=" ")
            answer(possible)
            if len(other_type) != 0:
                # If there are other items with the same type they are also printed
                print("You may, also, consider: ")
                answer(other_type, 1)
