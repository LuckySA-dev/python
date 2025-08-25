# class employee(object):
#     def __init__(self):
#         self.name = 'peter'
#         self._age = 45
#         self.__salary = 35000
    
# object1 = employee()
# print(object1.name)
# print(object1._age)
# print(object1.__salary)

class employee():
    def __init__(self):
        self.__maxearn = 30000
        
    def earn(self):
        print("earning is : {}".format(self.__maxearn))
        
    def setmaxearn(self, earn):
        self.__maxearn = earn
        
emp1 = employee()
emp1.earn()

emp1.__maxearn = 10000
emp1.earn()

emp1.setmaxearn(15000)
emp1.earn()
