# Inheritance and composition

In object-oriented programming, inheritance is the evil forest. Experienced programmers know to avoid this evil because they know that deep inside the Dark Forest Inheritance is the Evil Queen Multiple Inheritance. She likes to eat software and programmers with her massive complexity teeth, chewing on the flesh of the fallen. But the forest is so powerful and so tempting that nearly every programmer has to go into it and try to make it out alive with the Evil Queen’s head before they can call themselves real programmers. You just can’t resist the Inheritance Forest’s pull, so you go in. After the adventure you learn to just stay out of that stupid forest and bring an army if you are ever forced to go in again.

**Most of the uses of inheritance can be simplified or replaced with composition, and multiple inheritance should be avoided at all costs.**

What Is Inheritance?

Inheritance is used to indicate that one class will get most or all of its features from a parent class. Eg. class Foo(Bar), which says “Make a class Foo that inherits
from Bar.”

When you are doing this kind of specialization, there are three ways that the parent and child classes can interact:
1. Actions on the child imply an action on the parent.
2. Actions on the child override the action on the parent.
3. Actions on the child alter the action on the parent.

## Exercises

### Exercise 1 - Implicit Inheritance

The implicit actions that happen when you define a function in the parent but not in
the child.

1. Create a .py file and write the following:
    ```py
    class Parent():

        def implicit(self):
            print("PARENT implicit()")

    class Child(Parent):
        pass

    dad = Parent()
    son = Child()

    dad.implicit()
    son.implicit()
    ```
2. Run Script
    ```
    $ python ex44a.py 
    PARENT implicit()
    PARENT implicit()
    ```
#### Note

1. `pass` keyword tell python that you want an empty block.
2. This shows you that if you put functions in a base class (i.e., Parent), then all subclasses (i.e., Child) will automatically get those features. Very handy for repetitive code you need in many classes.

### Exercise 2 - Override Explicitly

The problem with having functions called implicitly is sometimes you want the child to behave differently. To do this just define a function with the same name in Child.

1. Create a .py file and write the following:
    ```py
    class Parent():

        def override(self):
            print("PARENT override()")

    class Child(Parent):

        def override(self):
            print("CHILD override()")

    dad = Parent()
    son = Child()

    dad.override()
    son.override()
    ```
2. Run Script
    ```
    $ python ex44b.py 
    PARENT override()
    CHILD override()
    ```
#### Note

1. In override explicitly, when same function define differently in base class and subclass, the subclass will override the function of base class.

### Exercise 3 - Alter Before or After

Now in this exercise, same function be created in both classes, but from within subclass function using `super` call function of base class.

1. Create a .py file and write the following:
    ```py
    class Parent():

        def altered(self):
            print("PARENT altered()")

    class Child(Parent):

        def altered(self):
            print("CHILD, BEFORE altered()")
            super().altered()
            print("CHILD, AFTER altered()")

    dad = Parent()
    son = Child()

    dad.altered()
    son.altered()
    ```
2. Run Script
    ```
    $ python ex44c.py 
    PARENT altered()
    CHILD, BEFORE altered()
    PARENT altered()
    CHILD, AFTER altered()
    ```

#### Note

1. `super` keyword - Typical use to call a cooperative superclass method/function.

```py
class Superfun(Child, BadStuff): pass
```
**Reason for `super()`:** whenever you have implicit actions on any SuperFun instance, Python has to look up the possible function in the class hierarchy for both Child and BadStuff, but it needs to do this in a consistent order. To do this Python uses “**method resolution order**” (MRO) and an algorithm called C3 to get it straight.

Because the MRO is complex and a well-defined algorithm is used, Python can’t leave it to you to get the MRO right. Instead, Python gives you the `super()` function, which handles all of this for you in the places that you need the altering type of actions

**Using super with __init__**: The most common use of `super()` is actually in __init__ functions in base classes. This is usually the only place where you need to do some things in a child, then complete the initialization in the parent. Here’s a quick example of doing that in the Child:

```py
class Child(Parent):

    def __init__(self, stuff):
        self.stuff = stuff
        super().__init__()
```
This is pretty much the same as the Child.altered, except I’m setting some variables in the __init__ before having the Parent initialize with its Parent.__init__

### Exercise 4 - all in one

This combined all above.

1. Create a .py file and write the following:
    ```py
    class Parent():

        def override(self):
            print("PARENT override()")

        def implicit(self):
            print("PARENT implicit()")

        def altered(self):
            print("PARENT altered()")

    class Child(Parent):

        def override(self):
            print("CHILD override()")

        def altered(self):
            print("CHILD, BEFORE altered()")
            super().altered()
            print("CHILD, AFTER altered()")

    dad = Parent()
    son = Child()

    dad.implicit()
    son.implicit()

    dad.override()
    son.override()

    dad.altered()
    son.altered()
    ```
2. Run Script
    ```
    $ python ex44d.py 
    PARENT implicit()
    PARENT implicit()
    PARENT override()
    CHILD override()
    PARENT altered()
    CHILD, BEFORE altered()
    PARENT altered()
    CHILD, AFTER altered()
    ```

###  Exercise 5 - composition

Inheritance is useful, but another way to do the exact same thing is just to use other classes and modules, rather than rely on implicit inheritance.

In composition, we use set variable in __init__ of class to take other classes method/function.

1. Create a .py file and write the following:
    ```py
    class Other():

        def override(self):
            print("Other override()")

        def implicit(self):
            print("Other implicit()")

        def altered(self):
            print("Other altered()")

    class Child():

        def __init__(self):
            self.other = Other()

        def implicit(self):
            self.other.implicit()

        def override(self):
            print("CHILD override()")

        def altered(self):
            print("CHILD, BEFORE altered()")
            self.other.altered()
            print("CHILD, AFTER altered()")

    son = Child()

    son.implicit()
    son.override()
    son.altered()
    ```
2. Run Script
    ```
    $ python ex44e.py 
    Other implicit()
    CHILD override()
    CHILD, BEFORE altered()
    Other altered()
    CHILD, AFTER altered()
    ```

## Note

**When to Use Inheritance or Composition**

You don’t want to have duplicated code all over your software, since that’s not clean and efficient.
- Inheritance solves this problem by creating a mechanism for you to have implied features in base classes.
- Composition solves this by giving you modules and the capability to call functions in other classes.

Three guidelines for when to do which:
1. Avoid multiple inheritance at all costs, as it’s too complex to be reliable. If you’re stuck with it, then be prepared to know the class hierarchy and spend time ﬁnding where everything is coming from.
2. Use composition to package code into modules that are used in many different unrelated places and situations.
3. Use inheritance only when there are clearly related reusable pieces of code that ﬁt under a single common concept or if you have to because of something you’re using.

[PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)