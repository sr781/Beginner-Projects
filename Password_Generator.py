import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


a = 0
a_str = ""
a_string_final = ""
string = ""
while a != nr_letters:
  a = a +1
  a_str = letters[random.randint(0,len(letters)-1)]
  a_string_final = a_string_final + a_str
a = 0
while a != nr_symbols:
  a = a +1
  a_str = symbols[random.randint(0,len(symbols)-1)]
  a_string_final = a_string_final + a_str
a = 0
while a != nr_numbers:
  a = a +1
  a_str = numbers[random.randint(0,len(numbers)-1)]
  a_string_final = a_string_final + a_str
print(a_string_final)
