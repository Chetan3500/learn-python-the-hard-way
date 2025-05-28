# Function can return something

Use of `return` in a function.

## Exercies

1. Create an ex21.py and write following content:
    ```py
    def add(a, b):
        print(f"ADDING {a} + {b}")
        return a + b

    def subtract(a, b):
        print(f"SUBTRACTING {a} - {b}")
        return a - b

    def multiply(a, b):
        print(f"MULTIPLYING {a} * {b}")
        return a * b

    def divide(a, b):
        print(f"DIVIDING {a} / {b}")
        return a / b

    print("Let's do some math with just funcitnos!")

    age = add(30, 5)
    height = subtract(78, 4)
    weight = multiply(90, 2)
    iq = divide(100, 2)

    print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

    print("here is a puzzle.")

    what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

    print(f"That becomes: {what} Can you do it by hand?")
    ```
2. Run script `python ex21.py` and output be:
```
Let's do some math with just funcitnos!
ADDING 30 + 5
SUBTRACTING 78 - 4
MULTIPLYING 90 * 2
DIVIDING 100 / 2
Age: 35, Height: 74, Weight: 180, IQ: 50.0
here is a puzzle.
DIVIDING 50.0 / 2
MULTIPLYING 180 * 25.0
SUBTRACTING 74 - 4500.0
ADDING 35 + -4426.0
That becomes: -4391.0 Can you do it by hand?
```

## Noted

Whatever `return` form a function can be as a value or argument.