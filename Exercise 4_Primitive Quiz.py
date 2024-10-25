"""
Exercise 4: Primitive Quiz
**********
"""

q1=input("What is the capital of France? ")
#Variable for question. User input to get answers from user. 
if q1=="Paris": #If else statement
    print("Correct Answer!") #Feedback when condition is True
else: #If else statement
    print("Incorrect Answer!") #Feedback when condition is False
    
    
"""
Advanced Requirements
"""
q1=input("What is the capital of France? ").upper() 
#Variable for question. User input to get answers from user. String upper() method to disregard user inputs' capitalizations
if q1=="PARIS": #If else statement
    print("Correct Answer!") #Feedback when condition is True
else: #If else statement
    print("Incorrect Answer!") #Feedback when condition is False

#Repeat the process from Question 1 for the rest of the questions
q2=input("What is the capital of Sweden? ").upper()
if q2=="STOCKHOLM":
    print("Correct Answer!")
else:
    print("Incorrect Anwswer!")
    
q3=input("What is the capital of Germany? ").upper()
if q3=="BERLIN":
    print("Correct Answer!")
else:
    print("Incorrect Answer!")
    
q4=input("What is the capital of Georgia? ").upper()
if q4=="TBILISI":
    print("Correct Answer!")
else:
    print("Incorrect Answer!")

q5=input("What is the capital of United Kingdom? ").upper()
if q5=="LONDON":
    print("Correct Answer!")
else:
    print("Incorrect Answer!")
    
q6=input("What is the capital of Spain? ").upper()
if q6=="MADRID":
    print("Correct Answer!")
else:
    print("Incorrect Answer!")
    
q7=input("What is the capital of Portugal? ").upper()
if q7=="LISBON":
    print("Correct Answer!")
else:
    print("Incorrect Answer!")
    
q8=input("What is the capital of Italy? ").upper()
if q8=="ROME":
    print("Correct Answer!")
else:
    print("Incorrect Answer!")
    
q9=input("What is the capital of Russia? ").upper()
if q9=="MOSCOW":
    print("Correct Answer!")
else:
    print("Incorrect Answer!")
    
q10=input("What is the capital of Greece? ").upper()
if q10=="ATHENS":
    print("Correct Answer!")
else:
    print("Incorrect Answer!")