#Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.

#Ask the user for input
fullname = input("Enter your fullname with leading spaces: ")

#Remove leading spaces and print the result
trimmed_name = fullname.lstrip()
print("Your name without leading space:", trimmed_name)