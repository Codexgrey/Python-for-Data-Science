## Sets
grocery_cart1 = {"Bread", "Oranges", "Jam", "Fruit Juice", "Eggs", "Butter", "Cookies"}
grocery_cart2 = {"Eggs", "Yam", "Grapes", "Cookies", "Apple", "Carrot", "Bread", "Ice Cream"}

# print(grocery_cart1)
# print(grocery_cart2);

grocery_cart2.discard("Yam")
grocery_cart2.add("Yoghurt")

# print(grocery_cart1)
# print(grocery_cart2);

merge_carts = grocery_cart1.union(grocery_cart2)
# print(merge_carts)


  #.update()
    # grocery_cart1.update(grocery_cart2)
    # print(grocery_cart1)


  #.copy()
backup_cart1 = grocery_cart1.copy()
backup_cart2 = grocery_cart2.copy()


#.difference() and .difference_update()
    # cart1_only = grocery_cart1.difference(grocery_cart2)
    # print(cart1_only)

    # grocery_cart2.difference_update(grocery_cart1)
    # print(grocery_cart2)


  #.intersection() and .intersection_update
backup_intersection = backup_cart1.intersection(backup_cart2)
# print(backup_intersection)

# print(backup_cart1)
# print(backup_cart2)

backup_cart1.intersection_update(backup_cart2)
# print(backup_cart1)


  #.symmetric_difference and .symmetric_difference_update
syd_carts = grocery_cart1.symmetric_difference(grocery_cart2)
# print(syd_carts)

    # grocery_cart1.symmetric_difference_update(grocery_cart2)
    # print(grocery_cart1)


## Dictionaries
customer_info = {
    "name": ["Mike Aubentraut", "Uzo Chuks", "Tom Whiteside", "Mary Jane"],
    "gender": ["Male", "Male", "Male", "Female"],
    "age": [22, 29, 34, 18],
    "nationality": ["American", "Nigerian", "Canadian", "Jamaican"]
}
# print(customer_info)

all_names = customer_info["name"]
# print(all_names)

all_nations = customer_info.get("nationality")
# print(all_nations)

all_keys = customer_info.keys()
# print(all_keys)

all_values = customer_info.values()
# print(all_values)

all_items = customer_info.items()
# print(all_items)

customer_info.update({"occupation": ["Actor", "Banker", "Footballer", "Experience Engineer"]})
# print(customer_info)


## Built-in Functions
    # get_data = input("Enter data here")
    # print(get_data)

# get_int = input("Enter data here: ")
# int_list = get_int.split(" ") 
# int_list.sort()
# smallest_int = int_list[0]
# second_smallest = int_list[1]
# print(smallest_int)
# print(second_smallest)


# get_data = input("Enter integers here: ")

# # Split str to list
# data_list = get_data.split(" ")

# # convert list items to int
# data_list[0] = int(data_list[0])
# data_list[1] = int(data_list[1])
# data_list[2] = int(data_list[2])
# data_list[3] = int(data_list[3])
# data_list[4] = int(data_list[4])

# smallest = min(data_list);
# print(smallest)

# smallest2 = data_list.index(sorted(data_list)[1])
# second_smallest = data_list[smallest2]
# print(second_smallest)

  #.zip()
# first_list = ['high', 'low', 'middle']
# second_list = [1, 2, 3]

# zipped_obj = zip(first_list, second_list)
# print(list(zipped_obj))

  #lambda(x:)
# modifier = lambda a: a.upper()
# output = modifier('voice')
# print(output)

# addUp = lambda x: x + 100
# output = addUp(99)
# print(output)

# doing_the_most = lambda x, y, z: (x**4 + y) / z
# output = doing_the_most(7, 3, 49)
# print(output)

  #map()
# scores = [45, 76, 49, 30]
# upgrade_scores = map(lambda c: c + 15, scores)
# upgraded_scores = list(upgrade_scores)
# print(upgraded_scores)

 #enumerate() and filter()
# num = [20, 31, 45, 60, 10, 77]
# numE = enumerate(num)
# outputE = list(numE)
# numF = filter(lambda c: c % 2 == 0, num)
# outputF = list(numF)
# print(outputE, outputF)

# rand_words = ["Emmanuel", "Pizza", "Coerce", "Smooth", "Laptop", "Screen"]
# check = "e"
# findingEve = filter(lambda c: check in c, rand_words )
# outWithEve = list(findingEve)
# print(outWithEve)


## Built-in Modules
 #time
# import time
# print('This is line 158')
# time.sleep(12)
# print('This is line 160')

 #random
import random as rd
# rd.seed(99)
# rand_words = ["Emmanuel", "Pizza", "Coerce", "Smooth", "Laptop", "Screen"]
# rd.shuffle(rand_words)
# # print(rand_words)

# randChoice = rd.choice(rand_words)
# print(randChoice)

# randPick = rd.sample(rand_words, 3)
# # print(randPick)

# feedback = rd.randrange(14, 44, 2)
# print(feedback)

 #datetime
from datetime import datetime as dt
currDatetime = dt.now()
# print(currDatetime)clear

currYear = currDatetime.year
# print(currYear) # similarly for minutes, month and seconds

output = currDatetime.strftime("%B%d%Y")
# print(output)

ch_day = "25/12/2021"
convert_date = dt.strptime(ch_day, "%d/%m/%Y")
# print(convert_date.date())

notable_days = ["15/1/2021", "14/2/2021", "1/4/2021", "29/5/2021", "12/6/2021", "1/10/2021", "25/12/2021"]
conND = map(lambda c: (dt.strptime(c, "%d/%m/%Y")).date().strftime("%d-%B-%Y"), notable_days)
new_notable_days = list(conND)
print(new_notable_days)

 #conditionals
randyWords = ["Emmanuel", "Pizza", "Coerce", "Smooth", "Laptop", "Screen"]
isgrthan7 = filter(lambda c: len(c) >= 7, randyWords)
grthan7 = list(isgrthan7)

# if grthan7:
#   # print('yes')
# else: 
#   # print('no')


# user_input = input('Give me a word: ')
# stringify = str(user_input)
# Setify = set(user_input)

# if len(stringify) == len(Setify):
#     print("No Duplicates")
# else:
#     print("Duplicates are present")

# check_duplicates = filter(lambda c: len(set(c)) != len (c), randyWords)
# duplicates = list(check_duplicates)
# print(duplicates)

# if duplicates:
#   print("YES! Duplicates")
# else:
#   print("NOPE! You've got to be kidding me")



 












