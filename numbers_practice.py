"""
Numbers exercises with Python
"""
## Complex numbers
# a = 2 + 3j
# print(a)

# print(complex(2))

## Binary
# print(bin(22))
## Octal
# print(oct(22))
## Hexadecimal
# print(hex(22))

## Modules
# import math
# from fractions import Fraction

# print(Fraction(1.5))
# print(math.factorial(5))
# print(math.exp(3))
# print(math.tan(90))

#* Exercise 1) NOT Gate - Build a function that simulates NOT gate. If the input is 0, it returns 1. And if it is 1, it returns 0. Do this without using logical, ternary, conditional or bitwise operators.
# def not_gate(digit):
#     return 1 - digit


# print(not_gate(0))

#* Exercise 2) Expanded - Write a function that expands a number. For instance, 1255 becomes 1000 + 200 + 50 + 5
# def expand_number(num):
#     num = str(num)
#     return ' + '.join([num[index] + '0' * (len(num) -1 -index) for index in range(len(num)) if num[index] != '0'])

# print(expand_number(66922))

#* Exercise 3) Dog Age Calculator - A dog's age, for the first two years, is said to be equal to 10.5 human years for each year. Every consequent year amounts to 4 human years. Write a function that takes the human age from the user and calculates the age in dog years.
# def dog_age_calculator(human_age):
#     assert(human_age >= 0)
#     return str((human_age) * 10.5 - ((human_age-2) > 0) * (human_age-2) * 6.5) + ' years'


# print(dog_age_calculator(9))

#* Exercise 4) Binary to Decimal - Write a function that takes a number in 1s and 0s considering it binary and returns its decimal equivalent.
def bin_to_dec(binary):
    decimal, mul = 0, len(str(binary))-1
    for digit in str(binary):
        decimal += int(digit) *2 ** mul
        mul -= 1
    return decimal


print(bin_to_dec(10))