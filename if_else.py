"""
If - else exercises from Data Flair course.
"""
#* Exercise 1) FizzBuzz - Write a program to print numbers 1 to 100, each on a new line
#* Print "Fizz" at the place of numbers multiples of 3
#* Print "Buzz" at the place of numbers multiples of 5
#* Print "FizzBuzz" at the place of numbers multiples of both 3 and 5
# def fizzbuzz():
#     for num in range(1, 101):
#         if num % 3 == 0: print("Fizz", end='');
#         if num % 5 == 0: print("Buzz"); continue
#         if num % 3 == 0: print(); continue
#         print(num)


# fizzbuzz()

#* Exercise 2) Double sum - Write a function that returns the sum of two integers. If, however, the first is twice the second, return twice their sum.
# def double_sum(a, b):
#     return (1 + int(a == 2 * b)) * (a + b)


# print(double_sum(20, 10))

#* Exercise 3) All Evens - Write a function that takes an inclusive interval from the user and returns all values where all digits are even.
# def all_evens(a, b, res=[]):
#     for num in range(a, b+1):
#         if all([int(digit) % 2 == 0 for digit in [char for char in str(num)]]):
#             res.append(num)

#     return res


# print(all_evens(200, 500))

#* Exercise 4) Up - Write a function that takes a list of integers and checks whether they are arranged in a strictly increasing order.
# def up(arr):
#     for index1 in range(len(arr)):
#         for index2 in range(index1 +1, len(arr)):
#             if arr[index1] >= arr[index2]:
#                 return False
    
#     return True

# print(up(['a','b','c','d','e','f']))
# print(up([5, 6, 7, 8, 9, 10, 11, 12]))
# print(up([55, 16, 81, 18, 20, 50, 111, 192]))
# print(up([1, 3, 5, 7, 9]))
