# Printing Printing

This and next exercise all about different way of printing.

## Exercise
1. Create ex7.py and write following content:
    ```py
    formatter = "{} {} {} {}"
    
    print(formatter.format(1, 2, 3, 4))
    print(formatter.format("one", "two", "three", "four"))
    print(formatter.format(formatter, formatter, formatter, formatter))
    print(formatter.format(
        "Try your",
        "Own text here",
        "This is 8th exercise",
        "out of 54 exercises"
        ))
    ```
2. On terminal run `python ex7.py`
3. Output be:
    ```
    1 2 3 4
    one two three four
    {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}
    Try your Own text here This is 8th exercise out of 54 exercises
    ```

## Experince

1. Using `.format()` i don't worry about filling `{}` which sometimes lead me to **NameError** and it easy to operate too.