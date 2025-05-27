# Parameter, Unpacking and Variable

Here few terms which every programmer know:
- **Module** - a single python file that contain python definitions, function, classes or variable.
- **Library** - is a collection of modules. eg. Numpy, requests, etc.
- **Argument/Parameter** - means values that going to be passed 

In this exercise, argument/parameter given in terminal at the time of executing file, then in program argv take this parameters and assign to variable which basically unpacking this parameters.

## Exercise
1. Create ex13.py and write following content:
```py
from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("The first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

```
2. On terminal run `python ex13.py hi bye tie`
3. Output be:
```
The script is called: exercise-13-parameter-unpacking-variable/ex13.py
The first variable is: hi
Your second variable is: bye
Your third variable is: tie
```

## Experiance

This time I need to gives input only in terminal while executing python file. As for my script output is differ from original because my current directory is parent directory of exercise directory.