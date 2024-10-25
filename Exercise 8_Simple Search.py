"""
Exercise 8: Simple Search
**********
"""

names=["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
#Create a variable to store the list
search="Sam" #Variable for the name being searched

if search in names: #If statement to check if the search variable is in names list
    print("Sam is in the list!") #Output if the if statement is true
else: #Else statement when the if statement is false
    print("Sam is not in the list.") #Output if the if statement is false
    

"""
Optional Requirements
"""

names=["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] 
#Create a variable to store the list
search=input("Please enter your selected Name: ") 
#User input method to ask the user to give a name. Variable to store the user input.  

if search in names: #If statement to check if the search variable is in names list
    print("Sam is in the list!") #Output if the if statement is true
else: #Else statement when the if statement is false
    print(f"{search} is not in the list.") #Output if the if statement is false