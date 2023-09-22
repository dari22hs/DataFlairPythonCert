"""
## zip() function
Built in function that returs a zip object whose __next__() method returns a tuple.
- It pairs corresponding elements from every argument.
- It stops when the shortest argument is exhausted.
"""
# for item in zip([1, 2, 3], ['red', 'green', 'blue']):
#     print(item)

# for item in zip([1, 2, 3]):
#     print(item)
    
# for item in zip([1, 2, 3, 4], [4, 5, 6], [7, 8, 9, 10]):
#     print(item)
    
# from itertools import zip_longest as zl
# print(set(zl([1, 2], [3, 4, 5]))) # Pairs 1, 2 ... 3, 4 ... None, 5

## Unzipping values (*)
# pairs = zip([1, 2, 3], ['a', 'b', 'c'], ['#', '*', '$'])
# nums, letters, chars = zip(*pairs)
# print(nums)
# print(letters)
# print(chars)

# new_pair = zip([1, 2], [3, 4, 5, 6])
# one, two = zip(*new_pair)
# print(one)
# print(two)

#* Exercise 1) Write a function that takes in a list of tuples and their prices. Make it return a list of items and another of their prices.
# def shopping_list(groceries):
#     items, prices = zip(*groceries)
#     return list(items), list(prices)


# print(shopping_list([('Oatmeal', 30), ('Milk', 40), ('Tuna', 20)]))

#* Exercise 2) A function takes in a list. Adjacent numbers don't like to stand together. Write a function that creates tuples from alternate numbers in the list.
# def create_tuples(myList):
#     return list(zip(myList[:], myList[2:]))


# print(create_tuples([1, 2, 3, 4, 5, 6, 7, 8, 9]))

#* Exercise 3) Write a function that takes in two integers of equal lengths. Return the sum of the distance between its individual digits.
# def calculate_distances(a, b):
#     assert len(str(a)) == len(str(b)), "Both numbers must have equal length."
#     return sum([abs(int(digit1) - int(digit2)) for digit1, digit2 in zip(list(str(a)), list(str(b)))])


# print(calculate_distances(714, 297))

#* Exercise 4) Write a function that takes in two strings holding name of students in two groups. For a group project, pair the students according to their roll numbers. There may only be two students in one group.
# def make_pairs(group1, group2):
#     group1, group2 = group1.split(','), group2.split(',')
#     for pair in zip(group1, group2):
#         print(f"{pair[0]} is with {pair[1]}.")


# make_pairs("Rick,Michael,Jim,", "Courtney,Jenn,Carol")
