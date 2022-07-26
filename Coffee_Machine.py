MENU = { #A dictionary containing the drink names as well as how much of each ingredient it requires 
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk" : 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = { #How much resources the coffee machine has
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

ascii_art = [
'''
      )  (
     (   ) )
      ) ( (
    _______)_
 .-'---------|  
( C|/\/\/\/\/|
 '-./\/\/\/\/|
   '_________'
    '-------'
''',

]

not_empty = True

def coin_counter():  # A function that asks the user how many coins they have added
  quarters = int(input("How many quarters (0.25)?: "))
  dimes = int(input("How many dimes? (0.10): "))
  nickles = int(input("How many nickles? (0.05): "))
  pennies = int(input("How many pennies? (0.01): "))
  total = ((0.25*quarters) + (0.1* dimes) + (0.05 * nickles) + (0.01 * pennies))
  return total

item = ["water", "milk", "coffee"]

while not_empty:
  
  check = True
  
  ask = input("What would you like to drink (espresso/latte/cappuccino)? Or would you like a report?: \n") # Prompts the user to enter a drink they want or of they would like to see what resources the machine has left
  enough = True
  if ask == "report": #This for loop goes through the "resources" dictionary and prints the resources
    for a in resources:
      print(f"{a}: {resources[a]}")

  
  elif ask == "espresso": #If the user enters "espresso" this elif statement is triggered
    for z in range(0,3): #This for loop makes sure there is enough resources to make the drink
      if resources[item[z]] < MENU["espresso"]["ingredients"][item[z]]:
        print(f"{item[z]} is too low") #If there isn't enough, it will show the user what is machine is low on
        check = False
    if check == True: #If there is enough to make a drink, then the user is shown the cost
      cost = MENU["espresso"]["cost"]
      print(f"It costs £{cost} for an espresso")
      money = coin_counter() #Then the coin_counter() function is triggered and the total amount is stored in the variable "money"
      
      if money >= cost: #This "if" statement checks to see if the value of coins entered, is equal to or exceeds the cost of the drink
        change = money - cost
        change = round(change, 2)
        print(f"Your change is £{change} \n") #Returns change to the user after calculation
        print(ascii_art[0])
        print("Here is your espresso! Enjoy \n")

      else:
        print("Not enough money \n")
        check = False

      if check == True: 
        for z in range(0,3):
          resources[item[z]] = resources[item[z]] - MENU["espresso"]["ingredients"][item[z]] #This for loop will take away the resource 
  

  elif ask == "latte":
    for z in range(0,3):
      if resources[item[z]] < MENU["latte"]["ingredients"][item[z]]:
        print(f"{item[z]} is too low")
        check = False
    if check == True:
      cost = MENU["latte"]["cost"]
      print(f"It costs £{cost} for a latte")
      money = coin_counter()
      
      if money >= cost:
        change = money - cost
        change = round(change, 2)
        print(f"Your change is £{change} \n")
        print(ascii_art[0])
        print("Here is your latte! Enjoy \n")

      else:
        print("Not enough money \n")
        check = False

      if check == True:
        for z in range(0,3):
          resources[item[z]] = resources[item[z]] - MENU["latte"]["ingredients"][item[z]]
    
    
  elif ask == "cappuccino":
    for z in range(0,3):
      if resources[item[z]] < MENU["cappuccino"]["ingredients"][item[z]]:
        print(f"{item[z]} is too low")
        check = False
    if check == True:
      cost = MENU["cappuccino"]["cost"]
      print(f"It costs £{cost} for a cappuccino")
      money = coin_counter()
      
      if money >= cost:
        change = money - cost
        change = round(change, 2)
        print(f"Your change is £{change} \n")
        print(ascii_art[0])
        print("Here is your cappuccino! Enjoy \n")

      else:
        print("Not enough money \n")
        check = False

      if check == True:
        for z in range(0,3):
          resources[item[z]] = resources[item[z]] - MENU["cappuccino"]["ingredients"][item[z]]    

  else:
    print("Power off")
    not_empty = False
