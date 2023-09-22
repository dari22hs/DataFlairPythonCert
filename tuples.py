"""
## Tuples
Collection of items that may be different, tuples are immutable and ordered.
"""
# a = 1,
# b = (1,)
# c = 1
# d = (1)
# print(type(a)) # Tuple
# print(type(b)) # Tuple
# print(type(c)) # Not a tuple, it's an integer
# print(type(d)) # Not a tuple, it's an integer

## Tuple packing
# a = 1, 2.0, 'three'

## Tuple unpacking
# percentages = (99, 97, 95, 99)
# a, b, c, d = percentages
# print(b) # Output is 97

## Accessing to elements
# myTuple = (1, 2, 3, 4, 5)
# print(myTuple[3])

## Slicing tuples
# percentages = (99, 97, 95, 92, 90, 98)
# print(percentages[2:4]) # Output (95, 92)
# print(percentages[:4]) # Output (99, 97, 95, 92)
# print(percentages[4:]) # Output (90, 98)
# print(percentages[2:2]) # Output ()

# print(percentages[:-2]) # Output (99, 97, 95, 92)
# print(percentages[-2:]) # Output (90, 98)
# print(percentages[2:-2]) # Output (95, 92)
# print(percentages[:]) # Output (99, 97, 95, 92, 90, 98)
# del percentages
# print(percentages) # Output -> NameError: name 'percentages' is not defined

## Reassigning tuples
# myTuple = (1, 2, 3, [6, 5])
# myTuple[3][0] = 4
# print(myTuple)

# myTuple2 = (1, 2, 300)
# print(min(myTuple2))
# print(max(myTuple2))
# print(sum(myTuple2))

# myTuple3 = ('hi', 'HI', 'hello')
# print(len(myTuple3))
# print(max(myTuple3))

# myTuple4 = ("", "0", "")
# myTuple5 = ("", 0, "")
# print(any(myTuple4))
# print(any(myTuple5))

# myTuple6 = ('1', 1, True, '')
# print(all(myTuple6))

#* Exercise 1) Write a function that takes in a list of fruits holding the number of apples and oranges - tuples of such numbers. Apples have 2 points and oranges have 3 points. Make the function return the total number of points for each case.
# def count_fruits(values):
#     results = dict()
#     for point in values:
#         results[point] = (2 * point[0]) + (3 * point[1])
#     return results


# print(count_fruits([(2, 3), (4, 3), (4, 7)]))

#* Exercise 2) Write a function that creates a tuple with a string, adding a counter to it each time until it reaches desired height.
# def create_pyramid(string, height):
#     myTuple = (string)
#     for index in range(1, height+1):
#         myTuple = (myTuple, index)
#         print(myTuple)


# create_pyramid("PYTHON", 10)
