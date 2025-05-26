# Comments

From `#` (Pound or Octothrope) onward python consider everthing comment which means python going to igonre it or not execute it.

## Exercise

1. Create ex2.py file and write following code:

    ```py
        # This line is a comment which not going to run and shown in o/p.
        # Since anything after # is ignored by python.

        print("This is going to print.") # This is not going to print.

        # Want to disable a line from execute put # at start
        # print("Not going to print")

        # do # give error or comment out if write middle of print statment
        print("No # error.")

    ```

2. On terminal run `python ex2.py`

3. Output shown:

    ```
        This is going to print.
        No # error.
    ```

## Issue

Well there is no issue for this simple exercise but if by mistakely I comment out a line which later need in code that gives an error.