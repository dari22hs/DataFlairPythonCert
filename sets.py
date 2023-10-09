"""
Sets
A set is an unordered collection of unique elements. Doesn't support duplicates.
A set is mutable but may not hold mutable items like lists and dictionaries or even other sets.
"""
# a = {1, 1, 2, 2, 3}
# b = {0, 1.5, 'two', 'two', 'TWO', 1.50, 1.500, 1.50000}
# print(f"{a} , {b}")
# c = set()
# print(c)

# print(a[1:3]) # TypeError: 'set' object is not subscriptable

# numbers = {1, 2, 3, 4, 5}
# ## discard() - Removes a specified element from the set. Does not raise an error if the element is not present in the set.
# numbers.discard(9) # Doesn't raise error when element is not found
# print(numbers)
# numbers.discard(1)
# print(numbers)

##remove() - Removes a specified element from the set. Raises a KeyError if the element is not present in the set.
# numbers.remove(9) # Raises KeyError when element is not found
# print(numbers)
# numbers.remove(2)
# print(numbers)

## pop() - Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.
# numbers.pop()
# print(numbers)

## clear()
# numbers.clear()
# print(numbers)

## add() - It is used to add a single element to the set. If the element is already in the set, it has no effect since sets only store unique elements.
# numbers.add(6)
# numbers.add((1, 2))
# print(numbers)

## update() - It is used to add multiple elements to the set. It takes an iterable (such as a list, tuple, or another set) as an argument and adds all the elements from the iterable to the set. Any duplicate elements are automatically removed.
# numbers.update([7, 8], {9, 10})
# print(numbers)

# days = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'}
# print(len(days))
# print(max(days))
# print(min(days))

# numbers = {1, 2, 3, 4, 5}
# print(sum(numbers))

# print(any({0})) # False
# print(any({0, '0'})) # True

# print(all({0})) # False
# print(all({'0', '1'})) # True

# print(set(sorted(numbers)))

## union() - Performs the union operation on two or more sets. Returns all the items that are in any of those sets.
set1, set2, set3 = {1, 2, 3, 4}, {4, 5, 6}, {4, 5, 6, 7}
# print(set1.union(set2, set3))

## intersection() - Performs the intersection operation on two or more sets. Returns all the items common in all sets.
# print(set1.intersection(set2))

## difference() - Returns a set that is the difference of two or more sets.
# print(set1.difference(set2))
# print(set2.difference(set1))

## symmetric_difference() - Returns a new set containing the elements that are in either of the sets but not in both.
# print(set1.symmetric_difference(set2))

## intersection_update() - Updates the set with the result of the intersection.
# set1.intersection_update(set2)
# print(set1)

## difference_update() - Updates the set with the result of the difference.
# set2.difference_update(set1)
# print(set2)

## symmetric_difference_update() - Updates the set with the result of the symmetric difference.
# set2.symmetric_difference_update(set3)
# print(set2)

## copy() - Creates a shallow copy of the set.
# set4 = set1.copy()
# print(set4)

## isdisjoint() - Returns True if two sets have a null intersection.
# print({1, 2}.isdisjoint({2, 3}))

## issubset() - Returns True if the set in the argument contains this set.
# print({1, 2}.issubset({1, 2, 3})) # True

## issuperset() - Returns True if the set contains the set in the argument.
# print({1, 2}.issuperset({1, 2, 3})) # False

## frozenset() - Is an immutable set that can be used as a key in a dictionary
# fz = frozenset([1, 2, 3])
# print({fz: 5})

#* Exercise 1) Write a function that takes two lists and gets the common values in both lists. Do this withouth using the intersection method.
# def common_values(list1, list2):
#     return set([num for num in list1 if num in list2])


# print(common_values([1, 2, 3], [3, 4, 5]))

#* Exercise 2) Write a function that takes in the ID's of people's subscriptions for service 'A' and service 'B', return the number of people who have at least one subscription.
# def subscribers(serviceA, serviceB):
#     return len(set(serviceA).union(set(serviceB)))


# print(subscribers([12, 22, 17, 95, 117, 1], [12, 87, 94, 664, 289, 200, 17]))