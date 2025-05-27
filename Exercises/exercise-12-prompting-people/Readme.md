# Prompting people

Similar as pervious exersice but in different way.

## Exercise

1. Create ex12.py and write following content:
    ```py
    age = input("How old are you? ")
    height = input("How tall are you? ")
    weight = input("How much do you weigh? ")

    print(f"So, you're {age} old, {height} tall and {weight} heavy.")
    ```
2. On terminal run `python ex12.py`
3. Output be:
    ```
    How old are you? 25
    How tall are you? 5.10
    How much do you weigh? 74
    So, you're 25 old, 5.10 tall and 74 heavy.
    ```

## Experiance

1. Now no need to use `print` keyword for asking question. `input()` take care of that.
2. In terminal, `pydoc3 [keyword]` keyworld like input gives doc of input. Similary for print `pydoc3 print`. I got error because of version so check version before running `pydoc3.x`. I also try for os and sys which is quite interesting.
