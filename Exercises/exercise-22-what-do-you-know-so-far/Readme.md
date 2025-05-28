# What do you know so far

1. `pydoc3.x [keyword]` tells what that keyword do. similar to `man` command of linux.
2. Keywords:
    - `#` - used for make a comment 
    - `print("prompt", end= ' ')` for printing and also decide how line ended.
    - `input("prompt")` for taking user input.
    - `'''...'''` or `"""..."""` for multi-line prompt or statement of string.
    - `f"...{}.."` use as a format string
        - `{}` carries values like 'string', 2 (digits), variable, etc.
    - `f"..{}..".format()`
        - `.format()` carries what values to put in `{}`.
    - `def funcName(arg1, arg2, ..., argN, *args):`
        - for defining function use `def`
        - `arg` take an argument,
        - `*args` take all arguments.
    - `funcName(para1, para2, ..., paraN)` - way of called out function.
    - `open(fileName, 'w/r')` - open a file for
        - `'w'` for write
        - `'r'` for read (set by default.)
    - `file.close()` - close a file
    - `file.read()` - read a file
    - `file.seek(0)` - move cursor in file
    - `file.readline()` - read only one line
    - `file.truncate()` - format or erase file
    - `file.write("statement")` - write in a file