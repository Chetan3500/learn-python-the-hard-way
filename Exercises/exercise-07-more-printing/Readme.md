# More Printing

## Exercise
1. Create ex7.py and write following content:
```py
print("Mary had a little lamb.")
print("Its fleecs was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10)

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end. Try removing it to see what happens
print(end1 + end2 + end3 + end4 + end4 + end5 + end6, end = ' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
```
2. On terminal run `python ex7.py`
3. Output be:
```
Mary had a little lamb.
Its fleecs was white as snow.
And everywhere that Mary went.
..........
Cheeese Burger
```

## Noted

1. In `print("Its fleecs was white as {}.".format('snow'))`, `'snow'` is a string. That's how python passes string in `.format()` without a variable.

2. `end = ' '` is tells how should the line ended and next line continued. That the reason in o/p there is a space between `Cheeese Burger`

3. `print("." * 10)`, here . get mutliply 10 times that's why o/p comes `..........`.
