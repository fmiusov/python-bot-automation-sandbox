# import argument module for script
from sys import argv

# designate how to parse arguments
script, filename = argv

# assign the txt variable as the function to open the filename argument received by argv
txt = open(filename)

# print first line telling user their filename title, then print the results of .read() called off the txt variable
print(f"Here's your file {filename}:")
print(txt.read())

# prompt the user to type their filename again, log the input under variable file_again
print("Type the filename again:")
file_again = input("> ")

# assign txt_again variable the file contents of file_again variable, ie the filename 
txt_again = open(file_again)

# print the the result of .read() of txt_again variable
print(txt_again.read())