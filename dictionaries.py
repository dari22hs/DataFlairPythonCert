"""
Dicitionaries.

Built-in data type used to store collections of key-value pairs. 
- Unordered
- Mutable
- Can't hold duplicate keys

"""
# Create a dictionary via comprehension
# myDict = {x * x: x for x in range(8)}
# myDict = {x: x * x for x in range(8)}

# print(myDict)

# dict2 = {1: 'apple', 'two': [1, 2, 3]}
# print(dict2)

# animals = {}
# animals[1] = 'dog'
# animals[2] = 'cat'
# animals[3] = 'turtle'
# print(animals)
# print(animals[2]) # KeyError when not found
# print(animals.get(1)) # Gets the value by using the key. Returns None if the key is not found.
# animals[3] = 8 # Reassign the value by using the key
# print(animals)
# animals[4] = 'tiger' # Add new key and value
# print(animals)
# del animals[3] # Delete single key-value pair
# print(animals)
# del animals # Delete whole dictionary
# print(animals) # NameError -> Because dictionary was deleted

# dict3 = {2: 'two', 3: 'three', 1: 'one'}
# print(len(dict3))
# print(all(dict3)) # Returns True if all keys have boolean value of True
# print(any(dict3)) # Returns True if at least one key have boolean value of True
# print(sorted(dict3)) # Returns a sorted list of all keys in ascending order
# print(dict3.keys()) # Returns a list of the keys in the dictionary
# print(dict3.values()) # Returns a list of the values in the dictionary
# print(dict3.items()) # Returns a list of the key-value pairs in the dictionary
# dict3.clear()
# print(dict3)

# dict4 = {1: 'a', 2: 'b', 3: 'c'}
# dict4copy = dict4.copy()
# dict4.clear()
# print(dict4copy)
# print(dict4copy.pop(8, -1)) # Removes specified key and displays removed value. Second argument (default) is optional, it's the value to display when the key is not found. Default value can be -1, None, 'Unknown', etc.
# print(dict4copy)
## popitem() - Removes and displays an arbitrary key-value pair.

## fromkeys() - Creates a new dictionary from the keys of an existing one
# newDict = dict4.fromkeys({1, 2, 5, 4}, 0)
# print(newDict)

## update() - Updates the dictionary to hold values from another (values it doesn't already contain)
# dict5 = {1: 1, 2: 2}
# dict6 = {2:2, 3:3}
# dict5.update(dict6)
# print(dict5)

# print(1 in dict5)
# print(8 in dict5)

## Iterate over a dictionary
# for key in dict5:
#     print(dict5[key]*2)
    
## Nested dictionary
# dict7 = {4: {1:2, 2:4}, 8:16} # A dictionary can be used as value
# print(dict7[4])

# dict8 = {{1:2, 2:4}:10, 8:16}
# print(dict8) # TypeError: unhasable type: 'dict' -> A dictionary cannot be used as a key.

#* Exercise 1) You are given a dictionary holding items from a store, and their prices. Write a function that returns the items with the highest price, the second-highest and the third-highest. If two items cost the same, include both.
# def costliest_three(items):
#     for item in [(item, price) for (item, price) in items.items() if price in sorted(items.values())[-3:]]:
#         print(item)


# costliest_three({'shoes': 79, 'jeans': 88, 'suit': 99, 'scarf': 25, 'socks': 8})

# #* Exercise 2) Write a function that takes a list of the names of students and assigns roll numbers to first names in a lexicographic order, then prints them out.
# def roll(names):
#     roll_nums = {sorted(names).index(name) + 1: name.split(' ')[0] for name in sorted(names)}
#     for roll in sorted(roll_nums):
#         print(roll, roll_nums[roll])


# roll(['Karl Josmain', 'Sarah Sue', 'Peggy Damper', 'Richard Genji', 'Peter Farm', 'Anne Wetherly'])