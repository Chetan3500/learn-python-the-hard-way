"Composition"

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
