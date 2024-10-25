"""
Exercise 5: Days of the Month
**********
"""

months={1:31,
        2:28,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31}
#Create a dictionary to store the months and the number of their days.
user_month=int(input("Enter your selected month in numeric form: "))
if user_month in months: #Nested If Statements
    print("Valid Month") #Output if the first if statement is true
    if user_month==1 or user_month==3 or user_month==5 or user_month==7 or user_month==8 or user_month==10 or user_month==12: 
    #Create conditions using if statement with comparational and logical operators
        print("The Month has 31 days") #Output of the if statement
    if user_month==4 or user_month==6 or user_month==9 or user_month==11:
    #Create conditions using if statement with comparational and logical operators
        print("The Month has 30 days") #Output of the if statement
    if user_month==2: #Creat condition using comparational operator
        print("The Month has 28 days") #Output of the if statement
else: #Else statement for the nested if statement
    print("Invalid Month Number") #Output of the else statement
    

"""
Advanced Requirement
"""

months={1:31,
        2:28,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31}
#Create a dictionary to store the months and the number of their days.
user_month=int(input("Enter your selected month in numeric form: "))
if user_month in months: #Nested If statements
    print("Valid Month") #Output if the first if statement is true
    if user_month==1 or user_month==3 or user_month==5 or user_month==7 or user_month==8 or user_month==10 or user_month==12:
    #Create conditions using if statement with comparational and logical operators
        print("The Month has 31 days") #Output of the if statement
    if user_month==4 or user_month==6 or user_month==9 or user_month==11:
    #Create conditions using if statement with comparational and logical operators
        print("The Month has 30 days") #Output of the if statement
    if user_month==2: #New nested if statement for new condition
        leap_year=input("Yes or No: Is the year a leap year? ").upper()
        #User input method to ask if the year is a leap year or not
        if leap_year=="YES": #If statement when true
            print("The Month has 29 days") #Output when true
        elif leap_year=="NO": #If statement when false
            print("The Month has 28 days") #Output when false 
else: #Else statement for the first nested if statement
    print("Invalid Month Number") #Output of the Else statement