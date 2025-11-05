
# Single level 

class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound.")

# Derived Class
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")

# Instance of Animal
animal = Animal('General Animal')
animal.speak()


# Instance Of Dog
dog = Dog('Dog')
dog.speak()

# -----------------------------------------------------------------------------------------

# Multi level inheritance

class Grandparent:
    def __init__(self,name):
        self.name = name

    def tell_story(self):
        print(f'{self.name} tells a story.')

# Intermediate class
class Parent(Grandparent):
    def work(self):
        print(f"{self.name} is working")


# Derived Class
class Child(Parent):
    def play(self):
        print(f"{self.name} is playing")

child = Child('Charlie')
child.tell_story()
child.work()
child.play()

# -----------------------------------------------------------------------------------------

# Hierarchical inheritance