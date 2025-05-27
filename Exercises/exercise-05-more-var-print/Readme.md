# More Variable and Print

Using *format string* for print output

## Exercise

1. Create ex5.py and write following content:
    ```py
    my_name = "Chetan"
    my_age = 25
    my_height = 5.9
    my_weight = 74
    my_eyes = 'Brown'
    my_teeth = 'White'
    my_hair = 'Black'
    
    print(f"Let talk about {my_name}.")
    print(f"He's {my_height} feet tall.")
    print(f"He's {my_weight} kg heavy.")
    print("Actually that's not too heavy.")
    print(f"He's got {my_eyes} eyes and {my_hair} hair.")
    print(f"He's teeth are usually {my_teeth} depending on the coffee.")
    
    # this line is tricky, try to get it exactily right
    total = my_age + my_height + my_weight 
    print(f"If I add {my_height}, {my_age}, and {my_weight} I get {total}.")
    ```
2. On terminal run `python ex5.py`
3. Output be:
    ```
    Let talk about Chetan.
    He's 5.9 feet tall.
    He's 74 kg heavy.
    Actually that's not too heavy.
    He's got Brown eyes and Black hair.
    He's teeth are usually White depending on the coffee.
    If I add 5.9, 25, and 74 I get 104.9.
    ```

## Issues

1. **SyntaxError** due to misspelled of variable names.
