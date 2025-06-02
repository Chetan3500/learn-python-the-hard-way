# Doing things to lists

Here give little intro of `class` keyword and left a question how come `a.split(' ')` python consider it `split(a, ' ')`, which going to cover later.

This exercise based on list operations.

## Exercise

1. Create an ex38.py and write following:
    ```py
    ten_things = "Apples Oranges Crows Telephone Light Sugar"

    print("Wait there are not 10 things in that list. let's fix that.")

    stuff = ten_things.split(' ')
    more_stuff = ["Day", "Night", "Song", "Frisbee",
            "Corn", "Banana", "Girl", "Boy"]

    while len(stuff) != 10:
        next_one = more_stuff.pop()
        print("Adding: ", next_one)
        stuff.append(next_one)
        print(f"There are {len(stuff)} items now.")

    print("There we go: ", stuff)

    print("Let's do some things with stuff.")

    print(stuff[1])
    print(stuff[-1])
    print(stuff.pop())
    print(' '.join(stuff))
    print('#'.join(stuff[3:5]))
    ```
2. Run script
    ```
    $ python ex38.py 
    Wait there are not 10 things in that list. let's fix that.
    Adding:  Boy
    There are 7 items now.
    Adding:  Girl
    There are 8 items now.
    Adding:  Banana
    There are 9 items now.
    Adding:  Corn
    There are 10 items now.
    There we go:  ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar', 'Boy', 'Girl', 'Banana', 'Corn']
    Let's do some things with stuff.
    Oranges
    Corn
    Corn
    Apples Oranges Crows Telephone Light Sugar Boy Girl Banana
    Telephone#Light
    ```

# Noted

Lists may be constructed in several ways:

   * Using a pair of square brackets to denote the empty list: "[]"

   * Using square brackets, separating items with commas: "[a]", "[a, b, c]"

   * Using a list comprehension: "[x for x in iterable]"

   * Using the type constructor: "list()" or "list(iterable)"

Here are few function of list sequence were performed to know more `pydoc3.x LISTS` or `pydoc3.x SEQUENCES`.