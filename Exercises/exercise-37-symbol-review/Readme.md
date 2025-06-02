# Symbol review

Python symbol and keyboard.

## Keywords

|keyword|Description|Example|
|:---:|:---|:---
|`and`|Logical and.| Ture and False == False|
|`as`|Part of the with-as statement|with X as Y: pass|
|`assert`|Assert (ensure) that something is ture.|assert False, "Error!"|
|`break`|stop this loop right now.|while True: break|
|`class`|Define a class|class Person(object)|
|`continue`|Don't process more of the loop, do it agian|while True: continue|
|`def`|Define a function|def X(): pass|
|`del`|Delete from dictionary|del X[Y]|
|`elif`|Else if condition|if: X; elif: Y; else: J|
|`else`|Else condition|if: X; elif: Y; else: J|
|`except`|If an exception happens, do this|except ValueError as e: print(e)|
|`exec`|Run a string as Python|exec 'print("Hello")'|
|`finally`|Exceptions or not, finally do this no matter what|finally: pass|
|`for`|Loop over a collection of things.|for X in Y: pass|
|`from`|Import specific parts of a module.|from x import y|
|`global`|Declare that you want a global variable|global x|
|`if`|if condition|if: X; elif: Y; else: J|
|`import`|Import a module into this one to use|import os|
|`in`|Part of for-loops. Also a test of X in Y|for x in y: pass also 1 in [1] == True|
|`is`|Like == to test equality|1 is 1 == True|
|`lambda`|Create a short anonymous functino|s = lambda y: y ** y; s(3)|
|`not`|Logical not|not True == False|
|`or`|Logical or|True or False == True|
|`pass`|This block is empty|def empty(): pass|
|`print`|Print this string|print('this string')|
|`raise`|Raise an exception when things go wrong|raise ValueError("No")|
|`return`|Exit the function with a return value|def X(): return y|
|`try`|try this block, and if exception, got to except|try: pass; except: pass|
|`while`|While loop|while x: pass|
|`with`|with an expression as a variable do|with x as y: pass|
|`yield`|Pause here and return to caller|def x(): yield y; x().next()|

## Data Types

|keyword|Description|Example|
|:---:|:---|:---|
|`True`|True boolean value|True or False == True|
|`False`|False boolean value|True and False == False|
|`None`|no-value or nothing|x = None|
|`bytes`|stores bytes, maybe of text, PNG, file, etc.|x = b"hello"|
|`strings`|Stores textual information|x = "hello"|
|`numbers`|Stores integers|i = 100|
|`floats`|Stores decimals|i = 10.234|
|`lists`|Stores a list of things|i = [1, 2, 'sdf']|
|`dicts`|Stores a key=value mapping of things|e = {'x': 1, 'y': 2}|

## String Escape Sequences

|Escape|Description|
|:---:|:---|
|`\\`|Backslash|
|`\'`|Single-quote|
|`\"`|Double-quote|
|`\a`|Bell|
|`\b`|Backspace|
|`\f`|Formfeed|
|`\n`|Newline|
|`\r`|Carriage|
|`\t`|Tab|
|`\v`|Vertical Tab|

## Operators

|Operator|Description|Example|
|:---:|:---|:---|
|`+`|Addition|2 + 4 == 6|
|`-`|Subtraction|2 - 4 == -2|
|`*`|Multiplication|2 *4 == 8|
|`**`|Power of|2 ** 4 == 16|
|`/`|Division|2 / 4 == 0.5|
|`//`|Floor division|2 // 4 == 0|
|`%`|modulus|2 % 4 == 2|
|`<`|less than|4 < 4 == False|
|`>`|more than|4 > 4 == False|
|`<=`|less than equal|4 <=4 == True|
|`>=`|more than equal|4 >=4 == True|
|`==`|||
|`!=`|||
|`()`|||
|`[]`|||
|`{}`|||
|`@`|||
|`,`|||
|`:`|||
|`.`|||
|`=`|||
|`;`|||
|`+=`|Add and assign|x = 1; x += 2|
|`-=`|Subtract and assign|x = 1; x -= 2|
|`*=`|Multiply and assign|x = 1; x *= 2|
|`/=`|Divide and assign|x = 1; x /= 2|
|`//=`|Floor divide and assign|x = 1; x //= 2|
|`%=`|Modulus assign|x = 1; x %= 2|
|`**=`|Power assign|x = 1; x **= 2|