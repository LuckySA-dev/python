# from abc import ABC, abstractmethod

# class employee(ABC):
#     def emp_id(self, id, name, age, salary):
#         pass
    
# class childemployee1(employee):
#     print("emp_id is 12345")
    
# emp1 = childemployee1()
# emp1.emp_id(id)

# from abc import ABC, abstractmethod
# class Absclass(ABC):
#     def print(self,x):
#         print("Passed value: ", x)
#     @abstractmethod
#     def task(self):
#         print("We are inside Absclass task")
        
# class test_class(Absclass):
#     def task(self):
#         print("We are inside test_class task")
        
# class example_class(Absclass):
#     def task(self):
#         print("We are inside example_class task")
        
# test_obj = test_class()
# test_obj.task()
# test_obj.print(100)

# example_obj = example_class()
# example_obj.task()
# example_obj.print(200)

# print("test_obj is instance of Absclass? ", isinstance(test_obj, Absclass))
# print("example_obj is instance of Absclass? ", isinstance(example_obj, Absclass))

class Dog:
    species = 'mammal'
    
    def calAge(self,age):
        print('Dog Age is {}'.format(age*3))
        
class SomeBread(Dog):
    pass

class SomeOtherBread(Dog):
    species = 'reptile'
    def calAge(self, age):
        print('Dog Age is {}'.format(age*4))
        
frank = SomeBread()
print(frank.species)
frank.calAge(5)

beans = SomeOtherBread()
print(beans.species)
beans.calAge(5)