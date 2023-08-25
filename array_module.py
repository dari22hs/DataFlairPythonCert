"""
## Array module.
Arrays are a collection of values, all of the same data type, stored in contiguous memory locations. This can make them more efficient than lists when you need to work with a large number of elements of a single data type.

Syntax:
Option 1) from array import array
Option 2) import array
"""
import array


arr = array.array('i', [7, 8, 9, 10, 10])
print(arr)

arr2 = array.array('u', 'Hey \u2641')
print(arr2)

print(arr.typecode)

print(arr.count(10))

arr.insert(0, 20) # [20, 7, 8, 9, 10, 10] -> Inserts number 20 at position 0
arr.pop(1) # [20, 8, 9, 10, 10] -> Pops the element at position 1, which is number 7
print(arr)

print(arr.tolist())
print(arr[2:4]) # [9, 10]