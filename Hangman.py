word_list = ["aardvark", "baboon", "camel"]
import random
chosen_word = random.choice(word_list) #A word is chosen at random using a function
print(chosen_word)
a = 0
lives = 6 #The player begins with 6 Lives

HANGMANPICS = [ '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
========='''] #This list contains the ascii art for the hangman

string = []
length = 0
while (a != len(chosen_word)): #This while loop will add an underscore for each letter in the "chosen_word" variable
    string.append("_")
    a = a + 1
while(True):
  guess = input("Enter a lowercase letter ") #The user is prompted to enter a letter
  a = 0
  word_in_list = False
  for letter in chosen_word: # This for loop goes through each letter in the "chosen_word" variable and assigns it to the "letter" variable  
    if (guess == letter): #If the word the user guessed is the same as the "letter" variable, this "if" statement is triggered
      string[a] = letter #It will assign the letter to the corresponding position of the list
      word_in_list = True #If a letter is found, this "word_in_list" boolean will be true
    a = a + 1
  if (word_in_list == False): #If the boolean "word_in_list" is False, this if statement is trigged and a life is taken away
    lives = lives - 1
    print("You lost a life, you currently have ", lives, "Remaining")
    print(HANGMANPICS[lives]) #This will print the ASCII art
  print(string)
  if (("".join(string)) == chosen_word): #If all the letters are correctly found, this if statement is triggered
    print("You Win")
    break
  elif(lives == 0): #If all lives are lost before all the letters are found, you lose
    print("No more lives, you lose")
    break
 
