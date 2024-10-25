"""
Exercise 10: Is it even?
***********
"""

def parity(num): #Defining the "parity" function with num as parameter
    if (num % 2) == 0: 
#If statement to check if the parameter will equal to zero when used in Modulo operator.
        print("The number is Even") #Output when the if statement is true
    else: #Else statement for the false
        print("The number is Odd") #Output when the if statement is false
#All 4 line above is part of the body of the function

user_number=int(input("Please enter an integer: "))
#User input with integer type to ask the user to give a number. Variable to store the user input

parity(user_number)
#Calling the function with the variable "user_number" as the substitute for the parameter
