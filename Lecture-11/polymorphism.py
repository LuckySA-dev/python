# class Animal:
#     def speak(self):
#         return NotImplementedError("Subclass must implement abstract method")
    
# class Dog(Animal):
#     def speak(self):
#         return "Wolf!"
    
# class Cat(Animal):
#     def speak(self):
#         return "Meow!"
    
# def make_animal_speak(animal):
#     print(animal.speak())
    
# dog = Dog()
# cat = Cat()

# make_animal_speak(dog)
# make_animal_speak(cat)

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        import math
        return math.pi * (self.radius ** 2)
    
shapes = [Rectangle(10,20), Circle(5)]

for shape in shapes:
    print(f"Area: {shape.area()}")