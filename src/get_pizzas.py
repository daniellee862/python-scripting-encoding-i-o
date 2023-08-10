import csv

# without context manager

get_pizza_file = open("../data/pizza.csv", "r", encoding="utf-8")

# extract the data from the csv file
# DONT NEED THIS IF USING READER OBJ
# read_pizza_file = get_pizza_file.read()

# prints a string of all data in csv file
# print(type(read_pizza_file))

# Now using csv reader so that we can return a reader object
pizza_reader_obj = csv.reader(get_pizza_file)

# prints an object : <_csv.reader object at 0x7fa2bed86c70>
# we knew its an iterable object because of the magic method __iter__
# print(pizza_reader_obj, dir(pizza_reader_obj))

# I cant iterate over the object without a context manager????
# IN order to iterate over the reader object we didnt need to > get_pizza_file.read() the file pointer is at the end of the file if we do this and there is no more data to read.
for row in iter(pizza_reader_obj):
    pass
    # print(row, "I AM NOT IN THE CONTEXT MANAGER ")

# close get_pizza_file so that it doesnt take space up in memory
get_pizza_file.close()


# LETS TRY WITH A CONTEXT MANAGERs
with open("../data/pizza.csv", "r", encoding="utf-8") as pizza_file:
    all_pizza_object = csv.reader(pizza_file)
    all_pizza_list = []

    for pizza_item in all_pizza_object:
        all_pizza_list.append(pizza_item)

# remove 'col-names'
dev_pizza_list = all_pizza_list[1:]
# get all pizzas
# print(dev_pizza_list)


# 1
# print("Diavola Price:", dev_pizza_list[2][1])

# 2
capri_description = dev_pizza_list[5][2]
# description is a string, it needs splitting into a list
capri_ingredients_list = capri_description.split(",")
for ingredient in capri_ingredients_list:
    pass
    # print(ingredient)

# 3
# list comprehension
# sorted() param1 is the sequence to sort (my list comprehension and filter), param2 is an option key by which to sort.
less_than_nine_asc = sorted(
    [pizza for pizza in dev_pizza_list if float(pizza[1].replace("£", "")) <= 9],
    key=lambda x: float(x[1].replace("£", "")),
)

# print(less_than_nine_asc)


# retype with open to get used to syntax;
# 4
with open("../data/pizza.csv", "r", encoding="utf-8") as pizza_file:
    all_pizza_object = csv.reader(pizza_file)
    dev_pizza_list = []

    for pizza_item in all_pizza_object:
        dev_pizza_list.append(pizza_item)


all_pizza_list = dev_pizza_list[1:]

# just a simple list comprehension with an 'if includes'
contains_mushrooms = [pizza for pizza in all_pizza_list if "mushrooms" in pizza[2]]
# print(contains_mushrooms)


# 5
with open("../data/pizza.csv", "r", encoding="utf-8") as pizza_file:
    all_pizza_object = csv.reader(pizza_file)
    dev_pizza_list = []

    for pizza_item in all_pizza_object:
        dev_pizza_list.append(pizza_item)


all_pizza_list = dev_pizza_list[1:]


table_cols = dev_pizza_list[0]
pizza_dicts = []

for pizza in all_pizza_list:
    pizza_dicts.append(
        {
            table_cols[0]: pizza[0],
            table_cols[1]: pizza[1],
            table_cols[2]: pizza[2],
            table_cols[3]: pizza[3],
        }
    )

# print(pizza_dicts)


# 6
with open("../data/pizza.csv", "r", encoding="utf-8") as pizza_file:
    all_pizza_object = csv.reader(pizza_file)
    dev_pizza_list = []

    for pizza_item in all_pizza_object:
        dev_pizza_list.append(pizza_item)


all_pizza_list = dev_pizza_list[1:]


daniels_pizza = [
    "Daniel's Special",
    "£12.99",
    "poached pear, flaked almonds, brie, chilli, egg, spinach",
    "1588kcal",
]
with open("../data/pizza.csv", "a", encoding="utf-8") as pizza_file:
    writer = csv.writer(pizza_file)
    writer.writerow(daniels_pizza)


# GOING TO END CSV HERE BECAUSE I WANT TO MOVE ON TO OTHER DATA TYPES AND COMPLETE AT LEAST ONE QUESTION FROM EACH TYPE.
