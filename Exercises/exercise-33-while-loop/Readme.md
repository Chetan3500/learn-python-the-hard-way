# Whlie loop

`while` loop keep executing the code block under it, as long as a Boolean expression is True.

## Exercise:

1. Create an ex33.py and write following content.
    ```py
    i, num = 0, []

    while i < 6:
        print(f"At the top i is {i}")
        num.append(i)

        i += 1
        print("Numbers now: ", num)
        print(f"At the bottom i {i}")

    print("The numbers: ")
    for n in num:
        print(n)
    ```
2. Run script
```sh
$ python ex33.py 
At the top i is 0
Numbers now:  [0]
At the bottom i 1
At the top i is 1
Numbers now:  [0, 1]
At the bottom i 2
At the top i is 2
Numbers now:  [0, 1, 2]
At the bottom i 3
At the top i is 3
Numbers now:  [0, 1, 2, 3]
At the bottom i 4
At the top i is 4
Numbers now:  [0, 1, 2, 3, 4]
At the bottom i 5
At the top i is 5
Numbers now:  [0, 1, 2, 3, 4, 5]
At the bottom i 6
The numbers: 
0
1
2
3
4
5
```

## Noted

1. Syntax

```py
while condition: # condition must be True for execute block of code
    statement
```
