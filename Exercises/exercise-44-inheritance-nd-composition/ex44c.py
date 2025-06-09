"Alter before or after"

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
