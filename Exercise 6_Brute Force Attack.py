"""
Exercise 6: Brute Force Attack
**********
"""

pwd="12345" #Variable to store the correct password
password=input("Please enter the password: ") #User input method to ask the user for the password
while password!=pwd: #While loop for when the user input is incorrect
    print('Incorrect Password! Please try again ') #Output if the while loop is true
    password=input() #Asks the user to input the password again
else: #Else statement for the "while loop" when the user input is correct
    print("Correct Password!") #Output when the user input is correct

"""
Optional Requirements
"""

chance=5 #Variable to store the limited attempt
pwd="12345" #Variable to store the correct password
password=input("Please enter the password: ") #User input method to ask the user for the password
while password!=pwd: #While loop for when the user input is incorrect
    chance-=1 #Decrement of the chance or attempt
    print(f"Incorrect Password! You have {chance} chance/s left: ") 
#Output when the user input is incorrect. Format printing to show the chances left
    password=input() #Asks the user to input the password again
    if chance<1: #The last attempt to be given to the user
        print("The maximum number of attempts has been reached and we have alerted the authorities!") 
            #Output when all the chances is used
        break; #Stops the loop
else: #Else statement for the "while loop" when the user input is correct
    print("Correct Password!") #Output when the user input is correct