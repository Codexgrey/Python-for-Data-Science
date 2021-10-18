# Loops
    ## while loop
# cracker = 1
# while (cracker < 5):
#     if cracker == 3:
#         print("I'm out the loop!")
#         break
#     else:
#         print('In the loop');
#         cracker += 1


#     # Guess game
# import random as rd

# get_data = input("Enter two integers here: ")
# convList = get_data.split(" ")

#     # converting to integers
# convList[0] = int(convList[0])
# convList[1] = int(convList[1])

#     # randomly selecting an integer within the range
# randInt = rd.randrange(convList[0], convList[1])

#     # time to guess
# correct_guess = 0
# while True:
#     user_guess = input("Enter your guess here: ")
#     if randInt == int(user_guess):
#         correct_guess = 0 + int(user_guess)
#         print(f"You guessed right. randInt = {correct_guess}")
#         break
#     elif int(user_guess) < randInt:
#         print("Guess is lower... try again")
#     elif int(user_guess) > randInt:
#         print("Guess is higher... try again")
#     else:
#         pass

    ## for loop
# new_list = ["pop", "rock", "country"]
# for item in new_list:
#     print(item)

# scores = [68, 90, 78, 71, 83]
# for num in scores:
#     if num % 2:
#         print(f"{num} is an Odd Number")
#     else:
#         print(f"{num} is an Even Number")


# customer_info = {
#     "name": ["Mike Aubentraut", "Uzo Chuks", "Tom Whiteside", "Mary Jane"],
#     "gender": ["Male", "Male", "Male", "Female"],
#     "age": [22, 29, 34, 18],
#     "nationality": ["American", "Nigerian", "Canadian", "Jamaican"]
# }

# # for entry in customer_info.items():
# #     print(entry[1][0])
# #     print("\n")

# continents = ["Africa", "Asia", "North America", "South America", "Europe", "Antartica", "Australia"]
# countries = [" Morocco", "China", "USA", "Argentina", "Croatia", "Eskimo", "New Zealand"]

# zipped_object = zip(countries, continents)

# for entry in zipped_object:
#     print(entry)
# for country_name, continent_name in zipped_object:
#     print(country_name)


    ## Class task
# get_int = input("Please enter integers: ")
# cnvlist = get_int.split(" ")

# map_obj = map(lambda c: int(c), cnvlist)
# int_list = list(map_obj)

# # intOutput = list(map(lambda c: round(c * 1.1, 1), map_obj))
# # print(intOutput)

# percentList = []
# for num in int_list:
#     num += (num * 0.1)  # OR num *= 1.1
#     percentList.append(num)
# print(percentList)
    

    ## Nested loops
# news = ['new', 'old', 'flashy']
# nouns = ['car', 'country', 'lady']
# adjectives = ['fast', 'beautiful', 'awesome']

# for info in news:
#     for qualifier in adjectives:
#         for thing in nouns:
#             print(info, qualifier, thing)
            
#     print("\n")


    # list comprehension
# scores = [60, 62, 77, 64, 66, 57, 91]
# upgraded_scores = [num + 3 for num in scores];
# print(upgraded_scores)

# new_upgrade = [num + 3 for num in scores if num % 2 == 0]
# print(new_upgrade)

new_list = [('Awesome', 12), ('Zebra', 2), ('Dawn', 9), ('New', 4)]
sorted_list = sorted(new_list, key = lambda c: c[1], reverse=True)
print(sorted_list)