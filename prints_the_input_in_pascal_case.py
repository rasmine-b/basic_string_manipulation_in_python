#Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.

#Ask the user for input
fullname = input("Enter your full name with incorrect casing: ")

#Convert to pascal Case and print the result
pascal_case_name = fullname.title().replace(" ", "")
print("Your name in Pascal Case:", pascal_case_name)