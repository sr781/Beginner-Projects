alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n") #Will the word be encrypted or decrypted?
text = input("Type your message:\n").lower() 
shift = int(input("Type the shift number:\n")) #How many charaters will each letter be shifted by


def ceasar_shift(text, shift, direction): #A definition with three arguments
  letter_alphabet_position = 0
  string = ""
  for letter in text: #Will go through each letter in the text
      for letter_compare in alphabet: #this for loop will check to see what position of the alphabet each letter is at. For example, the letter "c" is number 2 in the alphabet
        letter_alphabet_position = letter_alphabet_position + 1
        if letter == letter_compare:
          break
      if direction == "encode": #If "encode" is written, this if statement is run
        string = string + alphabet[(letter_alphabet_position + (shift-1))]
      elif direction == "decode": #If "decode" is written, this if statement is run
        string = string + alphabet[(letter_alphabet_position - (shift+1))] #Shifts letters backwards
      letter_alphabet_position = 0
  print(string)  #Whole string is printed
  
  
ceasar_shift(text, shift, direction) #To call the function
