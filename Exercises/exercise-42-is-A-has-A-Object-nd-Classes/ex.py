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
