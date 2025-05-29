# Memorizing Logic

Here introduce logic. For that let understand truth table (with keywords also try them on python interpreter):

1. `not` - Reverse the logic.

    |`not`|True?|
    |:---:|:---|
    |`not False`|`True`|
    |`not True`|`False`|

2. `or` - If anyone is `True`, result is `True`.

    |`or`|Ture?|
    |:---:|:---|
    |`False or False`|`False`|
    |`False or True`|`True`|
    |`True or False`|`True`|
    |`True or True`|`True`|

3. `and` - If anyone is `False`, result is `False`.

    |`and`|Ture?|
    |:---:|:---|
    |`False and False`|`False`|
    |`False and True`|`False`|
    |`True and False`|`False`|
    |`True and True`|`True`|

4. `not or` - reverse the `or` logic. If **both** are `False`, result is `True`.

    |`not or`|Ture?|
    |:---:|:---|
    |`not (False or False)`|`True`|
    |`not (False or True)`|`False`|
    |`not (True or False)`|`False`|
    |`not (True or True)`|`False`|

5. `not and` - reverse the `and` logic. If **both** are `True`, result is `False`.

    |`not and`|Ture?|
    |:---:|:---|
    |`not (False and False)`|`True`|
    |`not (False and True)`|`True`|
    |`not (True and False)`|`True`|
    |`not (True and True)`|`False`|

6. `!=` - If both *not* similar, result is `True`.

    |`!=`|True?|
    |:---:|:---|
    |`0 != 0`|`False`|
    |`0 != 1`|`True`|
    |`1 != 0`|`True`|
    |`1 != 1`|`False`|

7. `==` - If both similar, result is `True`.

    |`==`|True?|
    |:---:|:---|
    |`0 == 0`|`True`|
    |`0 == 1`|`False`|
    |`1 == 0`|`False`|
    |`1 == 1`|`True`|

All this above is basic Boolean algebra.