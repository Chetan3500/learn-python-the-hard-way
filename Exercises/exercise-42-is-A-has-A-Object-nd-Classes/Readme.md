# Is-A, has-A, Object and Classes

Let consider, jackie has a name of a salmon, and salmon which is a kind/type of fish.

Now can we said that in a school of fish there is a class of salmon and one salmon name is jackie. In code, we can say that salmon is-a fish and salmon has-a name jackie.

```py
class fish(): # class fish 
    pass

class salmon(fish): # class salmon is a fish

    def __init__(self, name):
        self.name = name    # name be jackie
    pass

jackie = salmon('jackie') # create object/instance of class salmon with para 'jackie'
```

In this exercise we learn about inheritance like how child inherit there parent traits. Just like in above example class fish which can have traits of fish like gills, mouth, etc. which give this traits to class salmon.

Two catch phrases: “is-a” and “has-a.”:
- Use the phrase is-a when you talk about objects and classes being related to each other by a class relationship. 
- Use the phrase has-a when you talk about objects and classes that are related only because they *reference* each other.



## Exercise

1. Create an ex42.py and copy the following content:
    ```py
    ## Animal is-a object
    class Animal(object):
        pass

    ## ??
    class Dog(Animal):

        def __init__(self, name):
            ## Dog has-a name
            self.name = name

    ## ??
    class Cat(Animal):

        def __init__(self, name):
            ## ??
            self.name = name

    ## ??
    class Person(object):
        def __init__(self, name):
            ## ??
            self.name = name
            ## ??
            self.pet = None

    ## ??
    class Employee(Person):

        def __init__(self, name, salary):
            ## super call __init__ method of superclass Person, passing name
            # super(Employee, self).__init__(name) # older version
            super().__init__(name)  # applicable for 3+ version of python
            ## ??
            self.salary = salary

    ## ??
    class Fish(object):
        pass

    ## ??
    class Salmon(Fish):
        pass

    ## ??
    class Halibut(Fish):
        pass

    ## rover is-a Dog
    rover = Dog("Rover")

    ## ??
    satan = Cat("Satan")

    ## ??
    mary = Person("Mary")

    ## ??
    mary.pet = satan

    ## ??
    frank = Employee("Frank", 120000)

    ## frank has-a pet which is-a rover 
    frank.pet = rover

    ## ??
    flipper = Fish()

    ## ??
    crouse = Salmon()

    ## ??
    harry = Halibut()
    ```
2. Run Script
    ```py
    ## Animal is-a object
    class Animal(object):
        pass

    ## Dog is-a Animal
    class Dog(Animal):

        def __init__(self, name):
            ## Dog has-a name
            self.name = name
            pass
        pass

    ## Cat is-a Animal
    class Cat(Animal):

        def __init__(self, name):
            ## Cat has-a name
            self.name = name
            pass
        pass

    ## Person is-a object
    class Person(object):
        def __init__(self, name):
            ## Person has-a name
            self.name = name
            ## Person has-a pet
            self.pet = None
            pass
        pass

    ## Employee is-a Person
    class Employee(Person):

        def __init__(self, name, salary):
            ## super call __init__ method of superclass Person, passing name
            # super(Employee, self).__init__(name) # older version
            super().__init__(name)  # applicable for 3+ version of python
            ## Employee has-a salary
            self.salary = salary
            pass
        pass

    ## Fish is-a object
    class Fish(object):
        pass

    ## Salmon is-a Fish
    class Salmon(Fish):
        pass

    ## Halibut is-a Fish
    class Halibut(Fish):
        pass

    ## rover is-a Dog
    rover = Dog("Rover")

    ## satan is-a Cat
    satan = Cat("Satan")

    ## Mary is-a Person
    mary = Person("Mary")

    ## mary has-a pet which is-a satan
    mary.pet = satan

    ## frank is-a Employee
    frank = Employee("Frank", 120000)

    ## frank has-a pet which is-a rover 
    frank.pet = rover

    ## flipper is-a Fish
    flipper = Fish()

    ## crouse is-a Salmon
    crouse = Salmon()

    ## harry is-a Halibut
    harry = Halibut()
    ```

## Noted

1. **is-a** showed direct connection between object and class.
2. **has-a** showed up when object and class releated by *refrenece*.
3. `super()` is used to called method/function of parent class.
4. `class Classname():` work fine in modern 3+ ver of python so no need to use `object` argument.