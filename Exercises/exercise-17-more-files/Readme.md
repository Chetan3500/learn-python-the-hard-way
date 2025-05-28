# More file

In this exercise Copying file is going to be practice.

## Exercise

1. Create a old_file.txt.
    ```sh
    echo "This is a test file." > old_file.txt
    ```
2. Create an ex17.py file and write following:
    ```py
    from sys import argv
    from os.path import exists

    script, from_file, to_file = argv

    print(f"Copying from {from_file} to {to_file}")

    # we could do these two on one line, how?
    in_file = open(from_file)
    indata = in_file.read()
    # indata = open(from_file).read()

    print(f"The input file is {len(indata)} bytes long")

    print(f"Does the output file exist? {exists(to_file)}")
    input("Ready, hit ENTER to continue, CTRL-C to abort.\n> ")

    out_file = open(to_file, 'w')
    out_file.write(indata)

    print("Alright, all done.")

    out_file.close()
    in_file.close()
    ```
3. On Terminal, `python ex17.py old_file.txt new_file.txt`
4. Output:
    ```
    Copying from old_file.txt to new_file.txt
    The input file is 21 bytes long
    Does the output file exist? False
    Ready, hit ENTER to continue, CTRL-C to abort.
    > 
    Alright, all done.
    ```
5. Check new_file.txt which copied of old_file.txt.

## Experiance

There are few new things I come across:

1. `os.path` - work like pwd for python.
2. `indata = open(from_file).read()` make simple if `in_file` not needed for other operation like write.
3. `len()` - gives total count of word present.
4. `exist` - check wheather new_file.txt present or not in pwd.