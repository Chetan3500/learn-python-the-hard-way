"file and function"

from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

curr_file = open(input_file)

print("First let's print the whole file:\n")
print_all(curr_file)
print("Now let's rewind, kind of like a tape:")
rewind(curr_file)
print("Let's print three lines:")

curr_line = 1
print_a_line(curr_line, curr_file)
curr_line = curr_line + 1
print_a_line(curr_line, curr_file)
curr_line = curr_line + 1
print_a_line(curr_line, curr_file)

curr_file.close()
