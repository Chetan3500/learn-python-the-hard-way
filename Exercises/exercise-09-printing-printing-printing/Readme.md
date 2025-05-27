# Printing, Printing, Printing



## Exercise
1. Create ex9.py and write following content:
    ```py
    days = "Mon Tue Wed Thu Fri Sat Sun"
    months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

    print("here are the days: ", days)
    print("here are the months: ", months)

    print("""
    There something going on here.
    With the three double-quotes.
    We'll be able to type as mush as we like.
      Even 4 lines if we want, or 5, or 6.
    """)
    ```
2. On terminal run `python ex9.py`
3. Output be:
    ```
    here are the days:  Mon Tue Wed Thu Fri Sat Sun
    here are the months:  Jan
    Feb
    Mar
    Apr
    May
    Jun
    Jul
    Aug

    There something going on here.
    With the three double-quotes.
    We'll be able to type as mush as we like.
      Even 4 lines if we want, or 5, or 6.

    ```

## Experiance

1. When `months` printed every month comes in next line due escape charater `\n`.

2. When `"""..."""` use for printing, the result comes same as written in program even space, {}, next line, etc. comes same. This `""".."""` also use for multi-line statement.