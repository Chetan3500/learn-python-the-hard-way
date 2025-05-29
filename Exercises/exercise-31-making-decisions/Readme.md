# Making decisions

This exercise like make a game. Another example for using keywords of: `if`, `elif` and `else`.

## Exercise

1. Create an ex31.py file and write the following:
    ```py
    print("""You enter a dark room with two doors.
    Do you go through door #1 or door #2?""")

    door = input("> ")

    if door == "1":
        print("There's a gaint bear here eating a cheese cake.")
        print("What do you do?")
        print("1. Take the cake.")
        print("2. Scream at the bear.")

        bear = input("> ")

        if bear ==  "1":
            print("The bear eats your face off. Good Job!")
        elif bear == "2":
            print("The bear eats your legs off. Good Job!")
        else:
            print(f"Well, doing {bear} is probably better.")
            print("Bear runs away.")

    elif door =="2":
        print("You stare into the endless abyss at Cthulhu's retina.")
        print("1. Blueberries.\n2. Yellow jacket clothespins.\n3. Understanding revolvers yelling melodies.")

        insanity = input("> ")

        if insanity == "1" or insanity == "2":
            print("Your body survives powered by a mind of jello.\nGood job!")
        else:
            print("The insanity rots your eyes into a pool of muck.\nGood job!")

    else:
        print("You stumble around and fall on a knife and die. Good job!.")
    ```
2. Run script
    ```
    $ python ex31.py 
    You enter a dark room with two doors.
    Do you go through door #1 or door #2?
    > 2
    You stare into the endless abyss at Cthulhu's retina.
    1. Blueberries.
    2. Yellow jacket clothespins.
    3. Understanding revolvers yelling melodies.
    > 3
    The insanity rots your eyes into a pool of muck.
    Good job!
    ```
    Different approach
    ```
    $ python ex31.py 
    You enter a dark room with two doors.
    Do you go through door #1 or door #2?
    > 1
    There's a gaint bear here eating a cheese cake.
    What do you do?
    1. Take the cake.
    2. Scream at the bear.
    > 2
    The bear eats your legs off. Good Job!
    ```

## Noted

When there is an `if` condition within an `if`/`elif` condition they are referred as *nested condition*.