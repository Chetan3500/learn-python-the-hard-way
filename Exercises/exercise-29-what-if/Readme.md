# What if

This exercise introduce to first condition type keyword i.e `if`.

## Exercise

1. Create an ex29.py file and write following code:
    ```py
    ppl, cats, dogs = 20, 30, 15

    if ppl < cats:
        print("Too many cats! The world is doomed!")

    if ppl > cats:
        print("Not many cats! The world is saved!")

    if ppl < dogs:
        print("The world is drooled on!")

    if ppl > dogs:
        print("The world is dry!")

    dogs += 5

    if ppl >= dogs:
        print("Ppl are greater than or equal to dogs.")

    if ppl <= dogs:
        print("Ppl are less than or equal to dogs.")

    if ppl == dogs:
        print("Ppl are dogs.")
    ```
2. Run script, `python ex29.py` and Output be:
    ```
    Too many cats! The world is doomed!
    The world is dry!
    Ppl are greater than or equal to dogs.
    Ppl are less than or equal to dogs.
    Ppl are dogs.
    ```

## Noted

1. Syntax:
    ```py
        if condition:
            statement
    ```
    - If condition comes out be `True` then python *read* statement.
    - If condition comes out be `False` then python *ignore* statement.
