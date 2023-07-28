"""
Operators in Python
"""
#* Arithmetic Operators
# Addition (+)
# Substraction (-)
# Multiplication (*)
# Division (/)
# Exponentiation (**)
# Floor Division (//)
# Modulus (%)

#* Relational Operators
# Equal to (=)
# Not equal to (!=)
# Greater than (>)
# Less than (<)
# Greater or equal (>=)
# Less or equal (<=)

#* Assignment Operators
# Assign (=)
# Add and Assign (+=)
# Substract and Asign (-=)
# Divide and Asign (/=)
# Multiply and Asign (*=)
# Modulus and Asign (%=)
# Exponent and Asign (**=)
# Floor Divide and Asign (//=)

#* Logical Operators
# and -> Returns True if all conditions are True
# or -> Returns True if AT LEAST ONE condition is True
# not -> Inverts an expression's Boolean value

#* Membership Operators
# in -> Returns True if the value is member of a sequence
# not in -> Returns True if the value is NOT member of a sequence

#* Identity Operators
# is -> Returns True if two objects are the same
# is not -> Returns True if two objects are different

#* Bitwise Operators
# Binary AND (&) -> 3&4 = 0 (011 & 100)
# Binary OR (|) -> 2|3 = 3 (10|11)
# Binary XOR (^) -> 2^3 = 1
# Binary One's Complement (~) -> ~-3 = 2
# Binary Left-Shift (<<) -> 2<<2 = 8 (1000)
# Binary Right-Shift (>>) -> 3>>1 = 1

# print(5 and [])
# print(5 & [])
# print(4 & 8)
# print(0 & True)
# print(0b1110 & 0b101)
# print(6 | 1)
# print(6 ^ 3)
# print(~2)
# print(~45)
# print(3 << 2)
# print(3 >> 2)
# print(31 >> 3)

#* Exercise 1) Toggled Digits - Write a function that takes a number, toggles the digit at a specified position in its binary form, and returns the number that results.
# def toggle_digit(num, pos):
#     num ^= (1 << pos)
#     return num


# print(toggle_digit(4, 1))

#* Exercise 2) Doubles - Write a function that prints n number of items in a series. This series begins at 3 and doubles the number each time.
# def doubles(n):
#     num = 3
#     for _ in range(n):
#         num = eval(bin(num)) << 1
#         print(num)


# (doubles(5))

#* Exercise 3) Troubled Addition - Write a function that adds two numbers without using the + operator or the built-in sum() function.
# def add(a, b):
#     return a- ~b -1


# print(add(10, 12))

#* Exercise 4) Bitwise Swap - Write a function that takes two integers and swaps them before returning them.
# def bitwise_swap(a, b):
#     a ^= b
#     b ^= a
#     a ^= b
#     return a, b


# print(bitwise_swap(4, 8))

## Less-than operator (<)

# print(3 < 3.0)
# print(3.0 < 3)
# print('Panda' < 'panda')
# print(0.999999 < True)
# print((1, 2, 3) < (1, 3, 2))
# print(() < (0,))
# print((1, 'one') < (2, 'two'))
# print([0] < [False])

## Greater-than operator (>)
# print(3, 4, 5 > 3, 4, 5.0)
# print((3, 4, 5) > (3, 4, 5.0))

#* Exercise 5) Battle of Numbers - Write a function that takes a list and returns the greatest number that without using the max() function.
# def greatest_number(myList):
#     greatest = myList[0]
#     for num in myList:
#         if num > greatest: greatest=num
        
#     return greatest
    
    
# myList = [1, 2, 3, 4, 5, 978]
# print(greatest_number(myList))

#* Exercise 6) Anagrams - Write a function that takes two strings and checks whether they are anagrams. An anagram is a word or phrase formed by rearrenging the letters of another.
# def is_anagram(string1, string2):
#     return sorted(string1.lower()) == sorted(string2.lower())


# print(is_anagram("rail", "liar"))

#* Exercise 7) The Last Digit - Write a function that takes 3 integers and returns True if the last digit of the result of multiplication of the first two equals to the third digit.
# def check_last_digit(a, b, c):
#     return str(a*b)[-1] == str(c)[-1]


# print(check_last_digit(5, 3, 15))

#* Exercise 8) Tale of Twins - Write a function that takes in an integer, then checks whether it is greater than the integer that is its mirror image.
# def check_greater_than_mirror(num):
#     return num > int(str(num)[::-1])


# print(check_greater_than_mirror(73))

#* 
