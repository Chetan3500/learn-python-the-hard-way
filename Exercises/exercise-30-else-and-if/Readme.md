# Else and if

In previous exercise, you might noticed that once `if` condition turn out be `false` and python move onto next part of code.

In this exercise, we not only make full use of `if` condition but if next condition also matches the first `if` then that be solved by `elif` and if both condition turn out to be `False` then `else` statement get executed.

# Exercise

1. Create an ex30.py and write following:
    ```py
    ppl, cars, trucks = 30, 40, 15

    if cars > ppl:
        print("We should take the cars.")
    elif cars < people:
        print("We should not take the cars.")
    else:
        print("We can't decide.")

    if trucks > cars:
        print("That's too many trucks.")
    elif trucks < cars:
        print("Maybe we could take the trucks.")
    else:
        print("We still can't decide.")

    if ppl > trucks:
        print("Alright, let's just take the trucks.")
    else:
        print("Fine, let's stay home then.")
    ```
2. Run script, `python ex30.py` and output be:
    ```
    We should take the cars.
    Maybe we could take the trucks.
    Alright, let's just take the trucks.
    ```

## Noted

1. Syntax:
    ```py
    if condition:  
        statement
    elif condition:
        statement
    .
    .
    else:
        statement
    ```
    - `if` condition comes true, python execute statement and skip next conditions and else.
    - `elif` condition comes true, python execute statement and skip next conditions and else.
    - `else` be execute if all above condition be false.

Once any condition turn out to be `True` python going to execute statement and skip remaining condition and else.