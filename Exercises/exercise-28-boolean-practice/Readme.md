# Boolean practice

## Exercise

1. Checkout [try.txt](try.txt), then start python interpreter in Terminal.
2. Here is look after practice try.txt in terminal:
    ```
    >>> True and True
    True
    >>> False and True
    False
    >>> 1 == 1 and 2 == 1
    False
    >>> "test" == "test"
    True
    >>> 1 == 1 and 2 != 1
    True
    >>> True and 1 == 1
    True
    >>> False and 0 != 1
    False
    >>> True and 0 != 1
    True
    >>> True or 1 == 1
    True
    >>> not (True and False)
    True
    ```
    ```
    >>> not (1 == 1 and 0 != 1)
    False
    >>> # let try variation on above one
    >>> 1 == 1 # True
    True
    >>> 0 != 1
    True
    >>> True and True
    True
    >>> not (True)
    False
    ```

## Noted

Expression like `!=` and `==` can be use with words/string.