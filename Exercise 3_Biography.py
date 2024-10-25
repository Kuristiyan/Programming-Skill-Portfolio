"""
Exercise 3: Biography
**********
"""
personal_information={'Name:': 'Noel Christian A. Domondon', 
                      'Hometown:': 'San Marcelino',
                      'Age:': 18}
#Create a dictionary to store information in pairs
for key, value in personal_information.items(): #Use for loop to select keys and values
    print(f"{key} {value}") #Format printing


"""
Advanced Requirements
"""
user_details={'Name:':input("Please enter your name: "),
              'Hometown:': input("Please enter your hometown: "),
              'Age:': int(input("Please enter your numerical age: "))}
#Create a dictionary to store information. Use user input method with appropriate data type
for key, value in user_details.items(): #Use for loop to select keys and values
    print(f"{key} {value}") #Format printing