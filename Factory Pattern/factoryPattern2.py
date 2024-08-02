from abc import ABC, abstractmethod
#Products
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
    
#Concrete Products
class Dog(Animal):
    def speak(self):
        return "Woof!"
    
#Concrete Products    
class Cat(Animal):
    def speak(self):
        return "Meow!"

#Creator Class
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass

#Concrete Creator
class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()
    
#Concrete Creator
class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()

# Example usage:
dog_factory = DogFactory()
dog = dog_factory.create_animal()
print(dog.speak())  # Output: Woof!

cat_factory = CatFactory()
cat = cat_factory.create_animal()
print(cat.speak())  # Output: Meow!