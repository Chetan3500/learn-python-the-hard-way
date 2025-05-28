# Functions and files

More on function and files

# Exercise

1. Create a test.txt file with following content.
    ```
    This is line 1
    This is line 2
    This is line 3
    ```

2. Create an ex20.py file with following content:
    ```py
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
    curr_line += 1
    print_a_line(curr_line, curr_file)
    
    curr_file.close()
    ```
3. Run script, `python ex20.py test.py` and output be:
    ```
    First let's print the whole file:

    This is line 1
    This is line 2
    This is line 3

    Now let's rewind, kind of like a tape:
    Let's print three lines:
    1 This is line 1

    2 This is line 2

    3 This is line 3
    ```

## Noted

1. `f.readline()` - read one line until `\n` and wait for it's next execution of line.
2. `rewind()` does nothing because `f.seek(0)` just moving cursor in text file.