# class Animal:
#     def __init__(self, name):
#         self.name = name
        
#     def speak(self):
#         return "Some sound"
    
# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} says wolf!"

# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says meow!"
    
# dog = Dog("Buddy")
# cat = Cat("Whiskers")

# print(dog.speak())
# print(cat.speak())

# class Dog:
#     species = 'mammal'
    
#     def calAge(self,age):
#         print('Dog Age is {}'.format(age*3))
        
# class SomeBread(Dog):
#     pass

# class SomeOtherBread(Dog):
#     species = 'reptile'
#     def calAge(self,age):
#         print('Dog Age is {}'.format(age*4))
        
# frank = SomeBread()
# print(frank.species)
# frank.calAge(5)

# beans = SomeOtherBread()
# print(beans.species)
# beans.calAge(5)