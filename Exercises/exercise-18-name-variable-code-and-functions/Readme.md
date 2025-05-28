# Name, Variable, Code and Functions

Here function are introduce. *Functions* are like mini-script which accept paramters/arguments same as `argv` but inside the script.

`def` is used to create function.

## Exercise

1. Create an ex18.py and write the following:
    ```py
    # this one is like your scripts with argv
    def print_two(*args):
        arg1, arg2 = args
        print(f"arg1: {arg1}, arg2: {arg2}")

    # ok, that *args is actually pointless, we can just do this
    def print_two_again(arg1, arg2):
        print(f"arg1: {arg1}, arg2: {arg2}")

    # This just takes one argument
    def print_one(arg1):
        print(f"arg1: {arg1}")

    # this one takes no arguments
    def print_none():
        print("I got nothing.")

    print_two("Hello", "World")
    print_two_again("Hello", "World Again")
    print_one("First!")
    print_none()
    ```
2. Run script, `python ex18.py` and Output be:
    ```
    arg1: Hello, arg2: World
    arg1: Hello, arg2: World Again
    arg1: First!
    I got nothing.
    ```

## Noted

1. Function syntax
    ```py
    def funcname(arguments, ):
        pass
    ```
2. If arguments startwith `*` like `*args` it take all arguments just like `argv` of `sys` but from inside script not on terminal.
3. When called out or use function: `funcname()`
