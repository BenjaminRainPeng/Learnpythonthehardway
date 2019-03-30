#input varibles
from sys import argv

#define varibles
script, input_file = argv

#define a function to print the whole page
def print_all(f):
    print(f.read())

#define a funcation to print again
def rewind(f):
    f.seek(0)

#define a funcation that choosing which line to print
def print_a_line(line_count, f):
    print(line_count, f.readline())

#change the name of input_file for convenience
current_file = open(input_file)

#print the file
print("First let's print the whole file:\n")

print_all(current_file)

#print the file again
print("Now let's rewind, kind of like a tape.")

rewind(current_file)

#print three lines in turn
print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
