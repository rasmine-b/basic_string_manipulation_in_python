#Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.

#Ask the user for input
num = int(input("Enter a number (0-1000): "))

#Format the number as a 6-digit string with leading zeros and print the result
formatted_num = f"{num:06}"
print("Formatted number:", formatted_num)