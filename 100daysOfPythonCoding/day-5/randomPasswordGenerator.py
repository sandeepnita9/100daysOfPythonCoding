import random

print("Welcome to Password Generator")
print("*****************************")
letters = ['a', 'b', 'c', 'd','e','f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9','0']
symbols = ['!', '@', '#', '$', '&', '*', '(', ')', '.']

no_of_letters = int(input("How many letters you want in your password : "))
no_of_numbers = int(input("How many numbers you want in your password : "))
no_of_symbols = int(input("How many special character you want in your password : "))
password_list = []

for num in range(1, no_of_letters+1):
    password_list.append(random.choice(letters))

for num in range(1, no_of_numbers+1):
    password_list.append(random.choice(numbers))

for num in range(1, no_of_symbols+1):
    password_list.append(random.choice(symbols))

#print(password_list)
random.shuffle(password_list)
#print(password_list)
password = ""
for char in password_list:
    password += char

print(f"Your Password is : {password}")