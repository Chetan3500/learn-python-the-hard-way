# More practice

This exercise for recalled what I done at start of exercises.

## Exercise

1. Create an ex24.py and write following:
    ```py
    print("Let's practice everything.")
    print('You\'d need to know \'about escapes with // that do:')
    print('\n newlines and \t tabs.')

    poem = """
    \tThe lovely world
    wih logic so firmly planted
    cannot discern \n the needs of love
    nor comprehend passion from intuition
    and requires an explanation
    \n\t\twhere there is none.
    """

    print("-" * 14)
    print(poem)
    print("-" * 14)

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

    start_point /= 10

    print("We can also do that this way:")
    formula = secret_formula(start_point)
    # this is aan easy way to apply a list to a format string
    print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
    ```
2. Run script, `python ex24.py`
3. Output be:
    ```
    Let's practice everything.
    You'd need to know 'about escapes with // that do:

     newlines and 	 tabs.
    --------------

    	The lovely world
    wih logic so firmly planted
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
    ```