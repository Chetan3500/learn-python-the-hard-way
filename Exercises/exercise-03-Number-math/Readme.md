# Number and Math

Math Operators:

|Symbol|Means|
|:---:|:---:|
|`+`|Addition|
|`-`|Subtraction|
|`/`|Slash/Division|
|`*`|Astrisk/Multiply|
|`%`|Modules|
|`<`|Less-than|
|`>`|More-than|
|`<=`|Less-than-equal|
|`>=`|More-than-equal|

## Exercise

1. Create ex3.py and write following code.

    ```py
    print("I will now count my chickens:")

    print("Hens", 25 + 30 / 6)
    print("Roosters", 100 - 25 * 3 % 4)

    print("Now I will count the eggs:")

    print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

    print("Is it true that 3 + 2 < 5 - 7?")

    print(3 + 2 < 5 - 7)

    print("What is 3 + 2?", 3 + 2)
    print("What is 5 - 7?", 5 - 7)

    print("Oh, that why it's False")

    print("How about some more.")

    print("Is it greater?", 5 > -2)
    print("Is it greater or equal", 5 >= -2)
    print("Is it less or equal?", 5 <= -2)
    ```

2. Open terminal run: `python ex3.py`

3. Output be like:

    ```
    I will now count my chickens:
    Hens 30.0
    Roosters 97
    Now I will count the eggs:
    6.75
    Is it true that 3 + 2 < 5 - 7?
    False
    What is 3 + 2? 5
    What is 5 - 7? -2
    Oh, that why it's False
    How about some more.
    Is it greater? True
    Is it greater or equal True
    Is it less or equal? False
    ```

## Q&A

1. **How does % work?**

    Another way to say it is, “X divided by Y with J remaining.” For example, “100 divided by 16 with 4 remaining.” The result of % is the J part, or the remaining part i.e 4.

2. **What is the order of operations?**

    In the United States we use an acronym called PEMDAS which stands for Parentheses Exponents Multiplication Division Addition Subtraction. 