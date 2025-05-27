# Reading Files

Let read files.

“Hard coding” means putting some bit of information that should come from the user as a string directly in our source code. That’s bad because we want it to load other files later. The solution is to use argv or input to ask the user what file to open instead of hard coding the file’s name.

## Exercise
0. First make ex15_sample.txt file and write following content:
    ```
    This is stuff I typed into a file.
    It is really cool stuff.
    Lots and lots of fun to have in here.
    ```
1. Create ex15.py and write following content:
    ```py
    from sys import argv

    script, filename = argv

    txt = open(filename)

    print(f"Here you file {filename}:")
    print(txt.read())

    print("Type the filename again:")
    file_again = input("> ")

    txt_again = open(file_again)

    print(txt_again.read())
    ```

2. On terminal run `python ex15.py ex15_sample.txt`
3. Output be:
    ```
    Here you file ex15_sample.txt:
    This is stuff I typed into a file.
    It is really cool stuff.
    Lots and lots of fun to have in here.

    Type the filename again:
    > ex15_sample.txt
    This is stuff I typed into a file.
    It is really cool stuff.
    Lots and lots of fun to have in here.

    ```

