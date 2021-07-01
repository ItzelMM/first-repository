# Itzel Munoz Monroy PSID: 1888446
# Importing the Items class from my other file
import FinalProjectClass

# Opening all the input files and creating most of the output files
manufacturers = open("ManufacturerList.csv", "r")
rows_m = manufacturers.readlines()
prices = open("PriceList.csv", "r")
rows_p = prices.readlines()
dates = open("ServiceDatesList.csv", "r")
rows_d = dates.readlines()
full_inv = open("FullInventory.csv", "w")
dam_inv = open("DamagedInventory.csv", "w")
date_inv = open("PastServiceDateInventory.csv", "w")

# Creating empty lists and dictionaries that will be used later
names_all_items = {}
damages = {}
names = []
id_list = []
dates_dic = {}
dates_list = []
types_dict = {}
types_list = []
price_list = []

# Counting the number of types of items there are in the input
for row in rows_m:
    item1 = FinalProjectClass.Items()
    columns = row.split(",")
    item1.item_type = str(columns[2])
    item1.new_type(types_list)

# This loop goes through the input files and
# organizes the desired information for the output file
# using the Items class' attributes and methods
for row in rows_m:
    item = FinalProjectClass.Items()
    columns = row.split(",")
    item.item_id = str(columns[0])
    id_list.append(int(item.item_id))
    item.item_name = str(columns[1])
    names.append(item.item_name)
    item.item_type = str(columns[2])
    item.item_damage = str(columns[3])
    for row_p in rows_p:
        columns_p = row_p.split(",")
        if columns_p[0] == item.item_id:
            item.item_price = str(columns_p[1]).strip('\n')
    for row_d in rows_d:
        columns_d = row_d.split(",")
        if columns_d[0] == item.item_id:
            item.item_date = str(columns_d[1]).strip('\n')
    item.csv_line(names_all_items)
    item.type_line(types_dict)
    item.add_date(dates_dic, dates_list)
    item.add_damage(damages, price_list)

# This loop creates a file for each type of item and adds the appropriate info to them
id_list.sort()
for type_item in types_list:
    file_type = open("{}Inventory.csv".format(type_item), "w")
    for ID in id_list:
        for key in types_dict:
            if str(ID) == str(key):
                if str(type_item) in types_dict[key]:
                    type_atr = types_dict[key]
                    type_atr.remove(str(type_item))
                    type_line = ",".join(type_atr)
                    file_type.write(type_line)
    file_type.close()

# This loop adds the appropriate info to the FullInventory file
names.sort()
for name in names:
    n_line = names_all_items[name]
    full_inv.write(n_line)

# This loop adds the appropriate info to the PastServiceDateInventory file
dates_list.sort()
for date in dates_list:
    d_line = dates_dic[date]
    date_inv.write(d_line)

# This loop adds the appropriate info to the DamagedInventory file
price_list.sort(reverse=True)
for price in price_list:
    dam_line = damages[str(price)]
    dam_inv.write(dam_line)

date_inv.close()
dam_inv.close()
full_inv.close()
manufacturers.close()
prices.close()
dates.close()
