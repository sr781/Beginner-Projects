def add(n1, n2):  #A bunch of functions for the calculator which will either add, subtract, multiply or divide
  return n1 + n2
def subtract(n1, n2):
  return n1 - n2
def multiply(n1,n2):
  return n1*n2
def divide(n1,n2):
  return n1/n2

art = ''' 

Calculator by Sulav Rai

 __________
| ________ |
||12345678||
|""""""""""|
|[M|#|C][-]|
|[7|8|9][+]|
|[4|5|6][x]|
|[1|2|3][%]|
|[.|O|:][=]|
"----------" 

'''


operations = { #A dictionary 
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator(): #Recursion is used to call this function
    print(art)
    num1 = int(input("What's the first number?: ")) #User is asked to add first number
    ask = True
    while ask == True: #This while loop will keep running as long as the user does not exit
        num2 = int(input("Enter the next number "))
        for a in operations:
          print(a)
        operation_symbol = input("Pick an operation from the line above: ")
        calculation = operations[operation_symbol] #When a mathematical symbol is selected, its value pair is set to the variable "calculation"
        abb = calculation(num1,num2) #The function with the name corresponding to the variable "calculation" is called
        print(abb)
        num1 = abb
        asking = input("Would you like to continue? Y or N? ")
        if asking =="N":
            ask = False
            print("Program will clear and restart")
            calculator()
calculator()
