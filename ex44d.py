class Parent(object):

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
        print("CHILD, BEFORE PARENT altered()")
        super(Child,self).altered()
        # calling altered() from the parent class of "Child", which is "Parent"
        print("CHILD, AFTER PARENT altered()")

dad=Parent()
son=Child()

dad.implicit()
son.implicit() # inherited from "Parent" class

dad.override()
son.override() # uses the altered() function in the "Child" class

dad.altered()
son.altered()
