# Test

In this exercise, I need to solve error in ex26.txt file and make sure it run smoothly.

## Exercise

1. Download [ex26.txt](./ex26.txt) and solve the issues/errors.
2. Copy ex26.txt to ex26.py and after solved issue this is how it look like:
    ex26.py:
    ```py
    print("How old are you?", end=' ')
    age = input()
    print("How tall are you?", end=' ')
    height = input()
    print("How much do you weigh?", end=' ')
    weight = input()

    print(f"So, you're {age} old, {height} tall and {weight} heavy.")

    from sys import argv
    script, filename = argv

    txt = open(filename)

    print(f"Here's your file {filename}:")
    print(txt.read())

    print("Type the filename again:")
    file_again = input("> ")

    txt_again = open(file_again)

    print(txt_again.read())


    print('Let\'s practice everything.')
    print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

    poem = """
    \tThe lovely world
    with logic so firmly planted
    cannot discern \n the needs of love
    nor comprehend passion from intuition
    and requires an explanation
    \n\t\twhere there is none.
    """

    print("--------------")
    print(poem)
    print("--------------")


    five = 10 - 2 + 3 - 6
    print(f"This should be five: {five}")

    def secret_formula(started):
        jelly_beans = started * 500
        jars = jelly_beans / 1000
        crates = jars / 100
        return jelly_beans, jars, crates


    start_point = 10000
    beans, jars, crates = secret_formula(start_point)

    # remember that this is another way to format a string
    print("With a starting point of: {}".format(start_point))
    # it's just like with an f"" string
    print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

    start_point = start_point / 10

    print("We can also do that this way:")
    formula = secret_formula(start_point)
    # this is an easy way to apply a list to a format string
    print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



    people = 20
    cats = 30
    dogs = 15


    if people < cats:
        print("Too many cats! The world is doomed!")

    if people > cats:
        print("Not many cats! The world is saved!")

    if people < dogs:
        print("The world is drooled on!")

    if people > dogs:
        print("The world is dry!")


    dogs += 5

    if people >= dogs:
        print("People are greater than or equal to dogs.")

    if people <= dogs:
        print("People are less than or equal to dogs.")


    if people == dogs:
    print("People are dogs.")
    ```
    Output be:
    ```
    How old are you? 25
    How tall are you? 5'10
    How much do you weigh? 74
    So, you're 25 old, 5'10 tall and 74 heavy.
    Here's your file test.txt:
    This is test file.

    Type the filename again:
    > test.txt
    This is test file.

    Let's practice everything.
    You'd need to know 'bout escapes with \ that do 
     newlines and 	 tabs.
    --------------

    	The lovely world
    with logic so firmly planted
    cannot discern 
     the needs of love
    nor comprehend passion from intuition
    and requires an explanation

    		where there is none.

    --------------
    This should be five: 5
    With a starting point of: 10000
    We'd have 5000000 beans, 5000.0 jars, and 50.0 crates.
    We can also do that this way:
    We'd have 500000.0 beans, 500.0 jars, and 5.0 crates.
    Too many cats! The world is doomed!
    The world is dry!
    People are greater than or equal to dogs.
    People are less than or equal to dogs.
    People are dogs.
    ```
I also created test.txt file so argv get a file after import it from sys.