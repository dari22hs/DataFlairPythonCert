"""
Lists in Python.
## .- Collection of values of any type
## .- Mutable

"""
# colors = ['blue', 'green', 'red', 'yellow', 'black', 'white']
# colors[2:3] = ['purple', 'silver']
# colors[2:4] = ['purple', 'silver']
# colors[2:5] = ['purple', 'silver']
# print(colors)
# del colors # Deleting a list
# print(colors) # Error because now >>colors<< is not defined

# numbers = [[[1, 2], [3, 4], 5], [6, 7]]
# print(numbers[0][1][1])

# a, b = [3, 1, 2], [5, 4, 6]
# print(a+b)

# a = [1, 2]
# a *= 3
# print(a)

## List comprehension
# even = [2*i for i in range(1, 11) if i%3 == 0] 
# print(even)
# print(len(even))
# print(max(even))
# print(min(even))
# print(sum(even))

# a = [2, 1, 3]
# print(sorted(a))

# print(sorted(['hello', 'hell', 'Hello', 'Hell', 'HELL', 'helloo', 'HELLO']))

# a = [2, 1, 3]
# a.append(4)
# print(a) # Output -> [2, 1, 3, 4]
# a.insert(0, 5) # (index, value)
# print(a) # Output -> [5, 2, 1, 3, 4]
# a.insert(1, 2)
# print(a) # Output -> [5, 2, 2, 1, 3, 4]
# a.remove(2) # Removes the first instance of an item from the list
# print(a) # Output -> [5, 2, 1, 3, 4]
# a.pop() # Removes the last element of an item from the list if the index is not specified
# print(a) # Output -> [5, 2, 1, 3]
# a.pop(0) # Removes the element at the specified index
# print(a) # Output -> [2, 1, 3, 4]
# print(a.index(3)) # Returns the first matching index of the specified item - Output -> 2 -> Because number >>3<< is at index >>2<<
# print(a.count(2)) # Returns the count of the specified item - Output -> 1
# a.sort() # Sorts the list in ascending order
# print(a) # Output -> [1, 2, 3]
# a.reverse() # Sorts the list in descending order
# print(a) # Output -> [3, 2, 1]
# a.clear() # Empties the list
# print(a) # Output -> []

#* Exercise 1) Write a function that accepts a string of multiple words, then prints the words back to front.
# def back_to_front(myString):
#     return ' '.join(reversed(myString.split(' ')))


# print(back_to_front("Welcome to the machine"))

#* Exercise 2) Write a function that accepts some numbers into a list, then prints the ones appearing in the list more than once.

# numberList, dups = input("Enter numbers separated by comma: ").replace(" ", "").split(','), []
# # print(numberList)
# for num in numberList:
#     if numberList.count(num) > 1: dups.append(num)

# for num in set(dups): print(num)

#* Exercise 3) Ignoring words like 'honest' that don't begin with a vowel, yet go with the article 'an', write a function that prepends the proper indefinite article ('a' or 'an') to a noun.
# vowels = ['a', 'e', 'i', 'o', 'u']


# def add_indefinite_article(noun):
#     return 'an ' + noun if noun[0] in vowels else 'a ' + noun


# print(add_indefinite_article("fox"))

#* Exercise 4) Write a function to understand the color coding of 4-band resistors. It takes in the first three values (ignoring tolerance) and calculates the resistance in Ohms (Ω)
# color_codes = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']


# def calc_resistance(digit1, digit2, multiplier):
#     return str((color_codes.index(digit1) * 10 + color_codes.index(digit2)) * 10 ** color_codes.index(multiplier)) + ' Ohms'


# print(calc_resistance('red', 'red', 'brown'))

## List comprehension part #2
# print([i*2 for i in {3, 1, 2}])
# print(["Even" if i%2 == 0 else "Odd" for i in range(8)])
# print([num for num in range(11) if num % 2 == 0 if num % 3 == 0])

#* Exercise 5) Use list comprehension to build a function that returns multiples of 3 that are smaller than the number n.
# def threes(n):
#     return [item for item in range(n) if item % 3 == 0]


# print(threes(16))

#* Exercise 6) Write a function that asks the user to input a string of integers separated by white spaces. It then returns a tuple from these valuels
# def game_of_tuples():
#     s = input("Enter a string of integers separated by white spaces: ")
#     return tuple([int(item) for item in s.split(' ')])


# print(game_of_tuples())

#* Exercise 7) Write a function that takes in a list of integers and shifts all zeros to the end of the list.
# def shift_zeros(myList):
#     """
#     Shift all zeros to the end of a list while preserving the order of non-zero elements.

#     Args:
#         myList (list): The input list.

#     Returns:
#         list: The modified list with zeros shifted to the end.
#     """
#     zeros = myList.count(0)
#     myList = [val for val in myList if val != 0]
#     for _ in range(zeros): myList.append(0)
#     return myList


# print(shift_zeros([10, 1, 5, 8, 0, 66, 91, 0, -8, 0, 17, 22, 117, 0, 1985, 2]))

#* Exercise 8) Write a function that takes in a list of lists and concatenates all the immediate sublists into one.
# def concat_list(*lists):
#     return [i for l in lists for i in l]


# list1 = [1, 2, 3]
# list2 = [4, 5]
# list3 = [6, 7, 8]
# print(concat_list(list1, list2, list3))

#* Exercise 9) Write a function that multiplies each value in a list with the length of the list and returns that.
# def multiply_len_x_values(myList):
#     return [value * len(myList) for value in myList]


# print(multiply_len_x_values([1, 2, 3, 4, 5]))

#* Exercise 10) Write a function that, in a range, prints out numbers with all even numbers.
# def even_evens(start, end):
#     evens = []
#     for num in range(start, end+1):
#         if all(map(lambda x: x % 2 == 0, [int(digit) for digit in str(num)])): evens.append(num)
#     return evens


# print(even_evens(0, 100))

#* Exercise 11) Write a function that accepts a string of parentheses and extracts from it properly-closed group of parentheses.
# def parentheses(text):
#     groups, group = [], ''
#     count = 0
#     for char in text:
#         group += char
#         count = count + 1 if char == '(' else count -1
#         if count == 0:
#             groups.append(group)
#             group = ''
#     return groups


# print(parentheses('((()()))())()()()'))