# A Good First Program

## Exercise

1. Make a file ex1.py and write following code.

    ```py
        print("Hello World!")
        print("Hello Again")
        print("I like typing this.")
        print("This is fun.")
        print('Yay! Printing.')
        print("I'd much rather you 'not'.")
        print('I "said" do not touch this.')
    ```

2. Open terminal and change dir to ex1.py file location the run `python ex1.py`.

3. You get the output like:

    ```
        Hello World!
        Hello Again
        I like typing this.
        This is fun.
        Yay! Printing.
        I'd much rather you 'not'.
        I "said" do not touch this.
    ```

## Issue

1. When I try: `print("Hello)` or `print("Hello"` I got error:

```py
    print("hello.
          ^
    SyntaxError: unterminated string literal (detected at line 1)
```

2. When I try: `prit("Hello")`, I got:

```py
    prit("hello.")
    NameError: name 'prit' is not defined. Did you mean: 'print'?
```

### Issue Solution

1. Whenever **SyntaxError** comes check that specific line and correct syntax.

    ```py
        print("hello.")
    ```
    Output:
    ```
        hello.
    ```

2. Whenever **NameError** get look for **keywords** which might be misspelled. So by fixing `prit("hello.")` to `print("hello.")` solve this NameError issue.
