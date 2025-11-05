

# Base Class
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




# Super keyword

class animal:
    def __init__(self):
        self.name = "buddy"

    def speak(self):
        print(f"{self.name} makes a sound")


class dog(animal):
    def __init__(self,breed):
        super().__init__()
        self.breed = breed

    def speak(self):
        super().speak()
        print(f'{self.name} barks . It is a {self.breed}. ')


dog = dog('Golden Retreiver')
dog.speak()