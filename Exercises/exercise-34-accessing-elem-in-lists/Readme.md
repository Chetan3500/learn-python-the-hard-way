# Accessing element in list

List are like array. There index start with is 0 (zero) and if we count from last element then index be -1. Index is where element location present in list.

Here a simple eg:
```py
>>> elems =  ['elem1', 'elem2', 'elem3']
>>> elems[0]
'elem1'
>>> elems[1]
'elem2'
>>> elems[3]    # It gives IndexError because list size is upto 2.
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range # List size can be with len(elems)
>>> elems[2]
'elem3'
>>> elems[-1]
'elem3'
>>> elems[-2]
'elem2'
>>> elems[-3]
'elem1'
```

