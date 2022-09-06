def prime_checker(number): #The code to check if a number is prime is in the function "prime_checker()"
  is_prime = True
  for a in range(2, (number)): #Function goes through the numbers from 2 to 1 below the input number
    if (number%a == 0): 
      print(f"{number} is not a prime number") #If the remainder is "0" than the number is not prime.
      is_prime = False
      break
  if (is_prime == True): #If the number is prime, the boolean value for "is_prime" is left at "True" and this if statement is triggered
    print(f"{number} is a prime number")

n = int(input("Check this number: ")) 
prime_checker(number=n) #Calls the function "prime_checker()"
