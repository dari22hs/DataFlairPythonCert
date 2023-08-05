"""
Loops in Python.
-> while loop
-> for loop
"""
# friends = ['Jenna', 'Elly', 'John', 'Luke']
# for friend in friends:
#     print(f"Hello, {friend}.")
    
# for item in [1, 2, 3]:
#     print(item)

# for item in {1, 2, 3}:
#     print(item)
    
# for letter in 'keyword':
#     print(letter)

# list = ['Spanish', 'English', 'German']
# for language in range(len(list)):
#     print(list[language])

# for row in range(5):
#     for star in range(row + 1):
#         print('*', end="")
#     print()

# for row in range(5):
#     print((row + 1)*'*')

# for letter in "break":
#     print(letter)
#     if letter == "e": break

#* Exercise 1) Star Diamond - Write a function that prints out a diamond of stars, length 7.
# def star_diamond():
#     for row in range(4):
#         for space in range(3 - row):
#             print(' ', end='')
#         for star in range(row + 1):
#             print('*', end='')
#         for star in range(row):
#             print('*', end='')
#         print()
    
#     for row in range(3):
#         for space in range(row + 1):
#             print(' ', end='')
#         for star in range(3 - row):
#             print('*', end='')
#         for star in range(2 - row):
#             print('*', end='')
#         print()
        
# star_diamond()

#* Exercise 2) Matrix Multiplication - Write a function that takes in two multidimensional matrices, multiplies them, and returns the resulting matrix. If the matrices cannot be multiplied, declare so.
# def mm(m1, m2):
#     if len(m1[0]) != len(m2):
#         print("Matrices not compatible for multiplication")
#         return
#     result = [[0 for i in range(len(m2[0]))] for j in range(len(m1))]
#     for row in range(len(m1)):
#         for col in range(len(m2[0])):
#             for temp in range(len(m2)):
#                 result[row][col] += m1[row][temp] * m2[temp][col]
#     return result


# print(mm([[1, 2], [1, 2]], [[1, 2], [1, 2]]))

#* Exercise 3) Number Pyramid - Write a function that prints out the folowwing pyramid of numbers making use of loops.
# def num_pyramid(n):
#     num = 1
#     for rows in range(n):
#         for row in range(rows + 1):
#             print(num, end=" ")
#             num += 1
#         print()
        

# num_pyramid(4)

#* Exercise 4) Number Diagonal - Write a function that prints out the folowwing square with numbers in the diagonal.
# def num_diagonal():
#     for row in range(1, 6):
#         for col in range(1, 6):
#             if row == col: print(row, end="")
#             else: print(0, end="")
#         print()
        

# num_diagonal()

#* Exercise 5) High Low - Write a function thattakes an integer n and prints out a receding pyramid where each row first rises up to n, and then decreases.
def high_low(n):
    for row in range(1, n+1):
        for col in range(row, n+1):
            print(col, end="")
        for col in range(n-1, row-1, -1):
            print(col, end="")
        print()


high_low(5)