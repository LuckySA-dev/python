# class Dog:
#     species = 'mammal'
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def description(self):
#         return "{} is {} years old".format(self.name, self.age)
    
#     def speak(self, sound):
#         return "{} says {}".format(self.name, sound)
    
# mikey = Dog("Mikey", 6)

# print(mikey.description())
# print(mikey.speak("Gruff Gruff"))

# class Calculate_area:
    
#     def rectangle_area(self, w, h):
#         return w * h
    
#     @classmethod
#     def triangle_area(cls, b, h):
#         return 0.5 * b * h
    
#     @staticmethod
#     def circle_area(r):
#         return 3.14 * r * r
    
# cal = Calculate_area()
# cal_rec = cal.rectangle_area(4, 5)
# cal_tri = cal.triangle_area(4, 5)
# cal_circle = cal.circle_area(5)

# print('Rectangle Area = ', cal_rec)
# print('Triangle Area = ', cal_tri)
# print('Circle Area = ', cal_circle)

class StudentTest:
    def __init__(self, name, score1, score2, score3):
        self.name = name
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
        
    def sumScore(self):
        return self.score1 + self.score2 + self.score3
    
    def __str__(self):
        return 'Name:{}, Total of score: {}'.format(self.name, self.sumScore())
    
std1 = StudentTest('Jantra', 20, 30, 25)
print(std1.name, std1.sumScore())
print(std1)