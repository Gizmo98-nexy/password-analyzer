#Private , Protected and Public
class Demo:
    def __init__(self):
        self.public="Public"
        self._protected="Protected"
        self.__private="Private"

obj=Demo()
print("Public:", obj.public)
print("Protected:", obj._protected)

#ACCESSING PRIVATE USING MANGLING
print("Private:", obj._Demo__private)


#Multilevel Inheritance
class Grandparent:
    def show1(self):
        print("'Grandparent class")

class Parent(Grandparent):
    def show2(self):
        print("Parent class")

class Child(Parent):
    def show3(self):
        print("Child class")

obj = Child()
obj.show1()
obj.show2()
obj.show3()


#Multiple Inheritance
class Father:
    def show1(self):
        print("Father class")

class Mother:
    def show2(self):
        print("Mother class")

class Child:
    def show3(self):
        print("Child class")

obj = Child()
obj.show1()
obj.show2()
obj.show3()
