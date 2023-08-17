"""
Strings in Python
"""
# a = "Dogs are love"
# print(a[3:8])
# print(a[-2:])

#* Exercise 1) Write a function that takes a string and returns it while reversing the words that are 4 or more in length.
# def reverse_string(myString):
#     return ' '.join(word[::-1] if len(word) >= 4 else word for word in myString.split())


# print(reverse_string("Hello ! How's it going ? Are you doing OK ?"))

#* Exercise 2) Write a function that determines whether the number or string provided is a palindrome
# def is_palindrome(myInput):
#     return str(myInput) == str(myInput)[::-1]


# print(is_palindrome("radar"))

#* Exercise 3) Write a function that takes in full names and strips away everything but the first names.
# def print_first_name(fullName):
#     return [name.split()[0] for name in fullName]


# print(print_first_name(["Michael Scott", "Homer Simpson", "Franklin Roosevelt"]))

#* Exercise 4) Write a function that takes a list of strings and a string prefix and returns a list of strings beginning with that prefix.
# def prefixed(strings, prefix):
#     return [string for string in strings if string.startswith(prefix)]


# print(prefixed(['nine', 'non', 'none', 'nein'], 'no'))

#* Exercise 5) Write a function that takes in a person's height in cm and represents it in feet and inches.
# def get_person_height(height):
#     feet = height/30.48
#     inches = (feet%1) * 12
#     print(f'You are {int(feet)}\'{round(inches,1)} tall.')
    

# get_person_height(170)

#* Exercise 6) Write a function that takes a verb and converts it into its Gerund form.
# def to_gerund(verb):
#     if verb[-1] == 'e':
#         return f"{verb} becomes {verb[:-1]+'ing'}"
#     if verb[-3:] != 'ing':
#         return f"{verb} becomes {verb+'ing'}"
#     return verb


# print(to_gerund("take"))

#* Exercise 7) Write a function that takes in a string. Make it capitalize the letters with even ASCII values and turn to lowercase those with odd ASCII values.
# def even_caps(sentence):
#     s = ''
#     for char in sentence:
#         if char.isalpha() and ord(char) != 32:
#             if char.islower() and ord(char) %2 == 0:
#                 s += chr(ord(char)-32)
#             elif char.isupper() and ord(char) %2 != 0:
#                 s += chr(ord(char)+32)
#             else: s += char
#         else: s += char
#     return s


# print(even_caps("I love animals"))

#* Exercise 8) Write a function that takes in two lists. The first holds abbreviations and the second holds words. Make sure no abbreviation suggests more than one word in the second list.
# def abbreviations(abbs, words):
#     for abb in abbs:
#         count = 0
#         for word in words:
#             if word.startswith(abb):
#                 count += 1
#         if count != 1: return False
#     return True


# print(abbreviations(['h', 'hel', 'b'], ['help', 'hello', 'holy', 'biased', 'helium']))
# print(abbreviations(['ho', 'help', 'b', 'hell', 'heli'], ['help', 'hello', 'holy', 'biased', 'helium']))

# print("hi" < "ha")
# print("hey" < "hi")
# print('ba'*5 + 'na'*5)

#* Exercise 9) Write a function that determines whether a word is an isogram. An isogram is a word where no letter repeats. Spaces and hyphens are exempted from this rule.
# def isogram(word):
#     for letter in word:
#         if word.count(letter) > 1 and letter.isalpha(): return f"The word \"{word}\" is not an isogram."
#     return f"The word \"{word}\" is an isogram."


# print(isogram("Hello"))
# print(isogram("Print"))

#* Exercise 10) Write a function that checks whether a string is a pangram or not. A pangram is a sentece that has each letter in the English alphabet at least once.
# def pangram(myString):
#     for letter in "abcdefghijklmnopqrstuvwxyz":
#         if letter not in myString.lower():
#             return False
#     return True


# print(pangram("Good morning, my friend.")) # False
# print(pangram("The quick brown fox jumps over a lazy dog.")) # True

#* Exercise 11) Write a function that takes a sentence or a phrase, then analyzes it to determine whether each word in it is an isogram. Bear in mind that this analysis is case-insensitive.
# def super_isogram(sentence):
#     for word in sentence.split(' '):
#         for letter in word:
#             if word.count(letter.lower()) > 1:
#                 return False
#     return True


# print(super_isogram("The best of both worlds.")) # True
# print(super_isogram("See eye to eye.")) # False

#* Exercise 12) Write a function that takes in a sentence. Make it return the number of times a word has its first and last characters the same as those of the entire sentence.
# def same_subs(sentence):
#     count = 0
#     for word in sentence.split(' '):
#         if (word[0] + word[-1]).lower() == (sentence[0] + sentence[-1]).lower():
#             count += 1
#     return count


# print(same_subs("This was a good day and the tests were great too! The energy is tremendous"))
