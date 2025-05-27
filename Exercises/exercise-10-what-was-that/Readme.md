# What was that?

Let's talk about *escape character*. This charater start with `\` (blackslash) in a string.

In previous exercise, `\n` was used to make string output in multi-line. Similarly there are other here is the following in list.

|Escape|Character|
|:---:|:---|
|`\\`|Blackslash(\)|
|`\'`|Single-quote(')|
|`\"`|Double-quote(")|
|`\a`|ASCII bel (BEL)|
|`\b`|ASCII backspace (BS)|
|`\f`|ASCII formfeed (FF)|
|`\n`|ASCII linefeed (LF)|
|`\N{name}`|Character named name in the Unicode database (Unicode only)|
|`\r`|Carriage return (CR)|
|`\t`|Horizontal tab (TAB)|
|`\uxxxx`|Character with 16-bit hex value xxxx|
|`\uxxxxxxxx`|Character with 32-bit hex value xxxxxxxx|
|`\v`|ASCII vertical tab (VT)|
|`\000`|Character with octal value 000|
|`\xhh`|Character with hex value hh|

## Exercises

### Exercise 1
1. Create ex10-1.py and write following content:
    ```py
    tabby_cat = "\tI'm tabbed in ."
    persian_cat = "I'm split\non a line."
    backslash_cat = "I'm \\ a \\ cat."

    fat_cat = '''
    I'll do a list:
    \t* Cat food
    \t* Fishies
    \t* Catnip\n\t* Grass
    '''

    print(tabby_cat)
    print(persian_cat)
    print(backslash_cat)
    print(fat_cat)
    ```
2. On terminal run `python ex10-1.py`
3. Output be:
    ```
    	I'm tabbed in .
    I'm split
    on a line.
    I'm \ a \ cat.

    I'll do a list:
    	* Cat food
    	* Fishies
    	* Catnip
    	* Grass

    ```

### Exercise 2

1. Create ex10-2.py and write following content:
    ```py
    # Backslash
    print("Backslash: \\")

    # Single quote
    print('Single quote: \'')

    # Double quote
    print("Double quote: \"")

    # ASCII bel (may beep in some terminals)
    print("Bell (\\a): \a")

    # ASCII backspace
    print("Backspace: ABC\bD")

    # ASCII formfeed (rare, behaves like a page break in some contexts)
    print("Formfeed: ABC\fDEF")

    # ASCII newline
    print("Linefeed (newline): Line1\nLine2")

    # Unicode character by name (Python only)
    print("Unicode name (\\N{name}): \N{GREEK CAPITAL LETTER DELTA}")

    # Carriage return
    print("Carriage return: Hello\rWorld")

    # Horizontal tab
    print("Tab:\tColumn2")

    # Unicode with 16-bit hex
    print("Unicode 16-bit: \u03A9")

    # Unicode with 32-bit hex
    print("Unicode 32-bit: \U0001F600")

    # Vertical tab
    print("Vertical tab: A\vB")

    # Octal value
    print("Octal value: \101")

    # Hex value
    print("Hex value: \x41")
    ```
2. On terminal run `python ex10-2.py`
3. Output be:
    ```
    Backslash: \
    Single quote: '
    Double quote: "
    Bell (\a): 
    Backspace: ABD
    Formfeed: ABC
                 DEF
    Linefeed (newline): Line1
    Line2
    Unicode name (\N{name}): Δ
    Worldage return: Hello
    Tab:	Column2
    Unicode 16-bit: Ω
    Unicode 32-bit: 😀
    Vertical tab: A
                   B
    Octal value: A
    Hex value: A
    ```

## Experiance

1. Form exercise 1, `'''...'''` or `"""..."""` both has same function.
2. In exercies 2, understand behaviour of each escape character.
