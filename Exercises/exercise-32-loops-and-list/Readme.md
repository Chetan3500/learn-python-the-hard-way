# Loops and list

Now `for` loop is introduce and list which 

## Exercies

1. Create an ex32.py and write following:
    ```py
    the_count = [1, 2, 3, 4, 5]
    fruits = ['apples', 'oranges', 'pears', 'apricots']
    change = [1, 'pennies', 2, 'dimes', 3, 'quarter']

    # This first kind of for-loop goes through a list
    for num in the_count:
        print(f"This is count {num}")

    # same as above
    for fruit in fruits:
        print(f"A fruit of type: {fruit}")


    # also we can go through mixed lists too
    # notice we have to use {} since we don't know what's in it
    for i in change:
        print(f"I fot {i}")

    # we can also build lists first start with an empty one
    elements = []

    # then use the range function to do 0 to 5 counts
    for i in range(0, 6):
        print(f"Adding {i} to the list.")
        # append is a function that lists understand
        elements.append(i)

    # now we can print them out too
    for i in elements:
        print(f"Elements was: {i}")
    ```
2. Run script, `python ex32.py` and output be:
    ```
    This is count 1
    This is count 2
    This is count 3
    This is count 4
    This is count 5
    A fruit of type: apples
    A fruit of type: oranges
    A fruit of type: pears
    A fruit of type: apricots
    I fot 1
    I fot pennies
    I fot 2
    I fot dimes
    I fot 3
    I fot quarter
    Adding 0 to the list.
    Adding 1 to the list.
    Adding 2 to the list.
    Adding 3 to the list.
    Adding 4 to the list.
    Adding 5 to the list.
    Elements was: 0
    Elements was: 1
    Elements was: 2
    Elements was: 3
    Elements was: 4
    Elements was: 5
    ```

## Noted

1. Syntax:
    ```py
    list_variable_name = []     # created empty list
    list_variable_name = [val1, val2]   # with value
    list_variable_name.append('val3')   # add value
    for i in list_variable_name:
        statement
    ```
