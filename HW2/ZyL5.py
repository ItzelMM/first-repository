# Itzel Munoz Monroy PSID: 1888446
import csv

filename = input()

item_count = {}

with open(filename, "r") as csvfile:
    file_reader = csv.reader(csvfile)
    for row in file_reader:
        for position in range(len(row)):
            item = row[position]
            num = row.count(item)
            item_count[str(item)] = num

for key in item_count.keys():
    print(key, item_count[key])
