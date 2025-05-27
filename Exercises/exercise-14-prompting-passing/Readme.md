# Prompting and passing

This exercise also on `argv` and `input`.

## Exercise
1. Create ex14.py and write following content:
    ```py
    from sys import argv

    script, user_name = argv
    prompt = '> '

    print(f"Hi {user_name}, I'm the {script} script.")
    print("I'd like to ask you a few questions.")
    print(f"Do you like me {user_name}?")
    likes = input(prompt)

    print(f"Where do you live {user_name}?")
    lives = input(prompt)

    print("What kind of computer do you have?")
    computer = input(prompt)

    print(f"""
    Alright, so you said {likes} about likeing me.
    You live in {lives}. Not sure where that is.
    And you a have a {computer} computer. Nice.
    """)
    ```
2. On terminal run `python ex14.py yourname`
3. Output be:
    ```
    Hi yourname, I'm the ex14.py script.
    I'd like to ask you a few questions.
    Do you like me yourname?
    > No
    Where do you live yourname?
    > India
    What kind of computer do you have?
    > Asus

    Alright, so you said No about likeing me.
    You live in India. Not sure where that is.
    And you a have a Asus computer. Nice.

    ```

## Experiance

Nice, felt like using prompt.