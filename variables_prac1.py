"""
Data Flair course. Variables practice.
"""
#* 1) Integers Come in All Sizes - Write a function that takes in an integer and gets its length without using len() function.
# def get_int_length(num):
#     if num == 0:
#         return 1
#     elif num < 0:
#         num = -num
        
#     length = 0
#     while num > 0:
#         num //= 10
#         length += 1
        
#     return length

# num = 2
# length = get_int_length(num)
# print(f"The length of {num} is {length}")

#* 2) Decimal Combat - Write a function that works with two integers. Whichever the greater number, it subtracts from it the difference of the two numbers plus one. The number that diminishes to 0 first, loses. Declare the winner each time.
# def game_of_subtraction(a, b):
#     while a > 0 and b > 0:
#         difference = abs(a - b) + 1
#         if a > b:
#             a -= difference
#         else:
#             b -= difference
    
#     if a <= 0:
#         print("Player B wins!")
#     else:
#         print("Player A wins!")
        
#* 3) Area of a triangle - Write a function that takes, from the user, the length of the base and the height of a triangle. Make the function output the resulting area of the triangle as an integer
# def get_triangle_area(base, height):
#     return int(base * height * 0.5)


# result = get_triangle_area(7, 14)
# print(f"Area of the triangle: {result}")

#* 4) Fibonacci series - Write a function that takes, from the user, the number of numbers to print and then prints the Fibonacci series up to that length
# def print_fibonacci():
#     length = int(input("Enter the length of the Fibonacci series: "))
#     a, b = 0, 1
#     count = 0
#     while count < length:
#         print(a, end=", ")
#         count += 1
#         a, b = b, a + b
#     print("...")
    
# print_fibonacci()

#* 5) Next Perfect Square - A perfect square is an integer, the square root of which is also an integer. Write a function that takes in a non-negative integer and returns the next perfect square. If the integer, however, is not a perfect square itself, it makes it known.
# import math


# def find_next_perfect_square(num):
#     return (int(math.sqrt(num)+1)**2) if math.sqrt(num) % 1 == 0 else "Not a perfect square itself"


# print(find_next_perfect_square(4))

#* 6) Remove vowels - Write a function that takes a string and removes any vowels in it
# def remove_vowels(string):
#     new_string = ""
#     for letter in string:
#         if letter.lower() not in ['a', 'e', 'i', 'o', 'u']: new_string += letter
#     return new_string


# print(remove_vowels("She was driving MAD."))

#* 7) Volume of a sphere - Write a function that takes in a sphere's radius and calculates its volume rounded to two decimal places. You can import the value of pi from the math module for this.
# import math


# def calculate_sphere_volume(radius):
#     return round(4/3*math.pi*radius**3, 2)


# print(calculate_sphere_volume(5))

#* 8) Valid password - Write a function that determines whether a string makes for a valid password. For this, it must be at least 6 characters long and at most 12 characters long. It also must have at least one letter, one digit and one special character like $, %, #, @.
def valid_password(password):
    p = list(password)
    if len(password) < 6 or len(password) > 12: return False
    if not (any(i.isdigit() for i in p)): return False
    if not (any(i in '$%#@' for i in p)): return False
    if not (any(i.isalpha() for i in p)): return False
    return True


print(valid_password('A1$123'))
    
    