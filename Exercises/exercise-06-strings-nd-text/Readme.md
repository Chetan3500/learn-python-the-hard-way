# Strings and text

A string is usually a bit of text you want to display to someone or “export” out of the program you are writing.

This exercise introduce of `.format()` and `f"...{}.."` string formating.

## Exercise

1. Create ex6.py and write following content:
    ```py
    types_of_ppl = 10
    x = f"There are {types_of_ppl} type of people."

    binary = "binary"
    do_not = "don't"
    y = f"Those who know {binary} and those who {do_not}."

    print(x)
    print(y)

    print(f"I said: {x}")
    print(f"I also said: '{y}'")

    hilariouse = False
    joke_evaluation = "Isn't that joke so funny?! {}"

    print(joke_evaluation.format(hilariouse))

    w = "This is the left side of..."
    e = "a string with a right side."

    print(w + e)
    ```
2. On terminal run `python ex6.py`
3. Output be:
    ```
    There are 10 type of people.
    Those who know binary and those who don't.
    I said: There are 10 type of people.
    I also said: 'Those who know binary and those who don't.'
    Isn't that joke so funny?! False
    This is the left side of...a string with a right side.
    ```

## Noted

1. Trying this `joke_evaluation = "Isn't that joke so funny?! {}"` on *Terminal* gives **SyntaxError** since `{}` is empty or without any already defined variable.

2. If `+` use between strings, the strings get concat.