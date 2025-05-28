# Reading and Writing 

This exercise more about handling file. Here few method or funtion that needed:
- `close` - Closes the file.
- `read` - Read the file.
- `readline` - Reads just one line.
- `truncate` - Empty the file.
- `write('stuff')` - Write stuff in the file.
- `seek(0)` - Moves the read/write location to the beginning of the file.

## Exercise

1. Create a test.txt file.
2. Create a ex16.py file and write the following:
    ```py
    from sys import argv

    script, filename = argv

    print(f"We're going to erase {filename}.")
    print("If you don't want that, hit CTRL-C (^C).")
    print("If you do want tha, hit RETURN.")

    input("?")

    print("Opening the file...")
    target = open(filename, 'w')

    print("Truncating the file. Goodbye!")
    target.truncate()

    print("Now I'm going to ask you for three lines.")

    line1 = input("line1: ")
    line2 = input("line2: ")
    line3 = input("line3: ")

    print("I'm going to write these to the file.")

    target.write(line1)
    target.write('\n')
    target.write(line2)
    target.write('\n')
    target.write(line3)
    target.write('\n')

    print("And finally, we close it.")
    target.close()
    ```
3. In terminal run `python ex16.py test.text`
4. Output:
    ```
    We're going to erase test.txt.
    If you don't want that, hit CTRL-C (^C).
    If you do want tha, hit RETURN.
    ?
    Opening the file...
    Truncating the file. Goodbye!
    Now I'm going to ask you for three lines.
    line1: Mary had a little lamb
    line2: Its fleece was white as snow
    line3: It was also tasty
    I'm going to write these to the file.
    And finally, we close it.
    ```
5. Check test.txt
    ```
    Mary had a little lamb
    Its fleece was white as snow
    It was also tasty
    ```

## Noted

- `open(filename, 'w')` use for open file in write mode. There are other mode check `pydoc3.x open` for detail.
