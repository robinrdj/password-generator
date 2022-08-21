# Password Generator
import random

# creating lists for letters, numbers and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Welcoming and getting the no of letters, symbols and numbers they want
print("Welcome to the Password Generator!\n ")
no_of_letters = int(input("no of letters would u like in your password \n"))
no_of_symbols = int(input("no of symbols would u like in ur password\n"))
no_of_numbers = int(input("no of numbers would u like in ur password\n"))

# adding passwords to the list
password_list = []
for n in range(0, no_of_letters):
    password_list.append(random.choice(letters))
for n in range(0, no_of_symbols):
    password_list.append(random.choice(symbols))
for n in range(0, no_of_numbers):
    password_list.append(random.choice(numbers))

# shuffling and converting list to strings
password_in_string = ""
random.shuffle(password_list)
for chars in password_list:
    password_in_string += chars
print(password_in_string)
