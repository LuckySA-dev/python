from functools import reduce

numbers = [1,2,3,4,5,6,7,8,9,10]

squared_number = map(lambda x: x ** 2, numbers)

even_squared_number = filter(lambda x: x % 2 == 0, squared_number)

sum_of_even_squared_numbers = reduce(lambda x, y: x + y, even_squared_number)
print(sum_of_even_squared_numbers)