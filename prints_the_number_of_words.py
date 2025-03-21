#Create a program that ask the user to input a complete statement. Print the number of words in the input.

#Ask user for input
statement = input("Enter a complete statement: ")

#Split the statement into words and count them and print the result
word_count = len(statement.split())
print("Number of words in your statement:", word_count)
