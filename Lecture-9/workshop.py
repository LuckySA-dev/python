# try:
#     x = 1 / 0
# except ZeroDivisionError as e:
#     print(f"Error : {e}")
    
# print("End Program")

# filename = input('Enter a filename : ')
# try:
#     infile = open(filename, 'r')
    
#     content = infile.read()
    
#     print(content)
    
#     infile.close
    
# except IOError:
#     print('An error occurred trying to read')
#     print('the file', filename)
    
# print("End of program")

# try:
#     value = int(input("Enter a number: "))
#     result = 10 / value
#     print(result)
# except ValueError:
#     print("Invalid input! Please enter a number.")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")

# print("End of program")

# try:
#     value = int(input("Enter a number: "))
# except Exception as e:
#     print(f"An error occurred: {e}")
    
# print("End of program")

# try:
#     value = int(input("Enter a number : "))
#     result = 10 / value
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# else:
#     print(f"The result is {result}")
    
# try:
#     numerator = float(input("Enter the numerator: "))
#     denominator = float(input("Enter the denominator: "))
    
#     result = numerator / denominator
    
# except ZeroDivisionError:
#     print("Error: You cannot divide by zero.")

# except ValueError:
#     print("Error: Invalid input. Please enter numberic values.")
    
# else:
#     print(f"result: {result}")
    
# finally:
#     print("Execution completed, whether an exception occurred or not.")


# print("End of program")

# try:
#     value = int(input("Enter a number: "))
#     result = 10 / value
# except ValueError:
#     print("Invalid input! Please enter a number")
# except ZeroDivisionError:
#     print("Connot divide by zero!")
# else:
#     print(f"The result is {result}")
# finally:
#     print("Execution completed.")

