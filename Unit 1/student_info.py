#Requirements: Use input() to collect: first name, surname, age (as an integer), and a favourite number (as a float). Display a formatted greeting using an f-string: ‘Welcome, [Full Name]!’. Display the name in UPPERCASE using .upper() and in Title Case using .title(). Calculate and display the age in months (age × 12). Round the favourite number to 2 decimal places using round(). Print the data type of each collected value using type()

Firstname = input("What is your Firstname? ")
Surname = input("What is your Surname? ")
Age = int(input("What is your Age? "))
FavouriteNumber = float(input("What is your Favourite Number? "))

print(f"Welcome, {Firstname} {Surname}!")
print(f"Your name in uppercase is: {Firstname.upper()} {Surname.upper()}")
print(f"Your name in title case is: {Firstname.title()} {Surname.title()}")
print(f"You are {Age * 12} months old.")
print(f"Your favourite number rounded to 2 decimal places is: {round(FavouriteNumber, 2)}")
