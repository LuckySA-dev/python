# class Car:
#     wheels = 4
    
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
        
#     def start_engine(self):
#         return f"The engine of the {self.year} {self.make} {self.model} is now running."
    
#     def stop_engine(self):
#         return f"The engine of the {self.year} {self.make} {self.model} is now off."
    
# my_car = Car("Toyota", "Corolla", 2020)

# print(my_car.make)
# print(my_car.model)
# print(my_car.year)

# print(my_car.start_engine())
# print(my_car.stop_engine())

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False
        
    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return f"'{self.title}' has been checked out."
        else:
            return f"'{self.title}' is already checked out."
    
    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return f"'{self.title}' has been returned."
        else:
            return f"'{self.title}' was not checked out."

book1 = Book("1984", "George Orwell", "1234567890")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321")

print(book1.check_out())
print(book1.return_book())
print(book2.check_out())
