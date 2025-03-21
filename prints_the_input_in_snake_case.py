#Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.

#Ask the user for input
fullname = input("Enter your full name with incorrect casing: ")

#Convert to snake case and print the result
snake_case_name = fullname.lower().replace(" ", "_")
print("Your name in snake_case:", snake_case_name)