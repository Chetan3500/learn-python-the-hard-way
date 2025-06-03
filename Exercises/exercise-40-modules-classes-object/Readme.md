# Module, classes and object

The only special operation on a module is attribute access: "m.name", where *m* is a module and *name* accesses a name defined in *m*’s symbol table.

A class is a way to take a grouping of functions and data and place them inside a container so you can access them with the . (dot) operator.

In this just overview of class and next exerices learn more.

## Exercise

1. Create an ex40.py and write following
    ```py
    class Song(object):

        def __init__(self, lyrics):
            self.lyrics = lyrics

        def sing_me_a_song(self):
            for line in self.lyrics:
                print(line)

    happy_bday = Song(["Happy birthday to you",
        "I dont' want to get sued",
        "So I'll stop right there"])

    bulls_on_parade = Song(["They rally around tha family",
        "With pockets full of shells"])

    happy_bday.sing_me_a_song()

    bulls_on_parade.sing_me_a_song()
    ```
2. Run script
    ```
    $ python ex40.py 
    Happy birthday to you
    I dont' want to get sued
    So I'll stop right there
    They rally around tha family
    ```