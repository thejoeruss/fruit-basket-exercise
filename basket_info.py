# Required imports.

import csv, sys

# Opening bucket.csv

input_file = sys.argv[1]
basket = list(csv.DictReader(open(input_file, newline='')))

# Items in basket.

basket_count = len(list(basket))

if basket_count > 0:
    print("There are {} pieces of fruit in the basket.\n".format(basket_count))
elif basket_count == 1:
    print("There is 1 single fruit in the basket.\n")
else:
   print("The basket is empty.\n")

# Total fruit Types.

fruit_type_count = 0
fruit_types = []

for fruit in basket:
    if fruit['fruit'] not in fruit_types:
        fruit_types.append(fruit['fruit'])
        fruit_type_count += 1

if fruit_type_count > 0:
    print("There are {} types of fruit in the basket.\n".format(fruit_type_count))
elif fruit_type_count == 1:
    print("There is 1 type of fruit in the basket.\n")
else:
    print("The basket is empty.\n")

# Number of each type of fruit in descending order.

fruit_list = {}
for fruit in basket:
    if fruit['fruit'] not in fruit_list:
        fruit_list[fruit['fruit']] = 1
    else:
        fruit_list[fruit['fruit']] += 1

fruit_list = dict(sorted(fruit_list.items(), key=lambda item: item[1], reverse=True))

for k, v in fruit_list.items():
    print("{}(s): {}".format(k.capitalize(),v))

print()

# Characteristics and quantities of each fruit by type.
# Note: This is assuming characteristic1 and characteristic2 are intentionally mixed.
fruit_characteristics = []

for f in basket:
    fruit_characteristics.append(f['fruit'].capitalize() + " - " + f['characteristic1'].replace(" ", "") + ", " +  f['characteristic2'].replace(" ", ""))

fruit_characteristics_dict = {}

for f in fruit_characteristics:
    if f not in fruit_characteristics_dict:
        fruit_characteristics_dict[f] = 1
    else:
        fruit_characteristics_dict[f] += 1

fruit_characteristics_dict = dict(sorted(fruit_characteristics_dict.items(), key=lambda item: item[0]))

print("The characteristics of each fruit are:")
for k, v in fruit_characteristics_dict.items():
    print("{}: {}".format(v,k))

print()

# Have any fruit been in the basket for over 3 days?

old_fruit = {}
for fruit in basket:
    if int(fruit['days']) > 3:
        if fruit['fruit'] not in old_fruit:
            old_fruit[fruit['fruit']] = 1
        else:
            old_fruit[fruit['fruit']] += 1
    else:
        continue

if old_fruit:
    print("Fruit that's been in basket for more than 3 days:")
    for k, v in old_fruit.items():
        print("{}(s): {}".format(k.capitalize(),v))
