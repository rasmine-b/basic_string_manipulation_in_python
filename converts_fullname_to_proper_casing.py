#Create a program that ask the user to input their fullname in incorrect casing. Print the input in proper casing.

#Ask the user for input
fullname = input("Enter your fullname with incorrect casing: ")

#Convert to proper casing and print the result
proper_name = fullname.title()
print("Your fullname in proper casing:", proper_name)