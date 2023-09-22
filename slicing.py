"""
## Slicing in Python
Used when only certain parts of constructs like lists, tuples, range objects, byte objects and strings are needed.
- Slicing operator []
- slice() constructor creates a slice object representing the set of indices represented by:
    - slice(start, stop, step)
    #? start - where to begin (optional)
    #? stop - where to stop slicing (not inclusive)
    #? step - increment between each index (optional)
"""
# myList = [1, 2, 3, 4, 5]
# print(myList[1:4])

# print(slice(3))

# l = [1, 2, 3, 4, 5]
# print(l[slice(3)]) # Output -> [1, 2, 3]
# print(l[0:3]) # Output -> [1, 2, 3]
# print(l[:3]) # Output -> [1, 2, 3]

# s = 'helloworld'
# print(s[slice(1, 6, 2)])
# print(s[slice(1, 6)])
# print(s[slice(-5, -10, -1)])

# t = [1, 2, 3, 4, 5]
# print(t[:3])
# print(t[3:])
# print(t[:])
# print(t[::2])
# print(t[::-1])
# print(t[:5:2])

#* Exercise 1) Write a function that checks every other index in a string and returns True only if it contains any letter at least twice.
# def check_double_evens(string):
#     return any(filter(lambda letter: string[1::2].count(letter) > 1, string[1::2]))


# print(check_double_evens("hello world"))

#* Exercise 2) Write a function that takes two lists of equal lengths and interleaves their values. So it takes one value from list1, another value from list2, another value from list1 and so on until both lists exhaust.
# def two_lists(list1, list2):
#     temp = list1 * 2
#     # print(temp)
#     temp[::2] = list1
#     # print(temp)
#     temp[1::2] = list2
#     # print(temp)
#     return temp


# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9, 10]
# print(two_lists(list1, list2))

#* Exercise 3) Write a function that takes in a list of integers and returns True only if for each value in the list, the sum of the previous values is lesser.
# def greatest(list1):
#     for index1 in range(1, len(list1)):
#         if list1[index1] <= sum(list1[:index1]):
#             return False
#     return True


# print(greatest([2, 3, 4]))

#* Exercise 4) Write a function that takes in a word and a size, and breaks it down into substrings of the given size.
# def divide(word, size):
#     return [word[index: index + size] for index in range(0, len(word), size)]


# print(divide('lightweight', 3))