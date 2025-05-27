# Asking question

Here we take input from user.

## Exercise
1. Create ex11.py and write following content:
    ```py
    print("How old are you?", end=" ")
    age = input()
    print("How tall are you?", end=' ')
    height = input()
    print("How much do you weigh?", end=' ')
    weight = input()

    print(f"So, you'r {age} old, {height} tall and {weight} heavy.")
    ```
2. On terminal run `python ex11.py`
3. Output be:
    ```
    How old are you? 25
    How tall are you? 5.10
    How much do you weigh? 74
    So, you'r 25 old, 5.10 tall and 74 heavy.
    ```

## Experiance

This was simple and easy. When I removed `end= ' '` the input comes in next line. And I also read about coversion by using `int(input())` which change floating decimal into integer.