# file = open("example.txt", "w")

# file.close()

# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)\

# with open("example.txt", "w") as file:
#     file.write("Hello World!\n")
#     file.write("This is a new line.\n")

# with open("example.txt", "a") as file:
#     file.write("This line is append. \n")
   
# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content) 

# with open("example.txt", "r") as file:
#     line = file.readline()
#     while line:
#         print(line.strip())
#         line = file.readline()
        
# with open("example.txt","r") as file:
#     lines = file.readlines()
#     for line in lines:
#         print(line.strip())

# import os

# os.remove('employees.txt')

# os.rename('example.txt', 'philosophers.txt')

# import struct

# record = (1, 'Jane Doe', 20, 3.75)

# with open("records.bin", "wb") as file:
    
#     data = struct.pack('i20sif', record[0], record[1].encode(), record[2], record[3])
    
#     file.write(data)
    
# import struct

# num_records = int(input("How many records do you want to create? "))

# with open("records.bin", "wb") as file:
#     for _ in range(num_records):
#         id_num = int(input("Enter ID: "))
#         name = input("Enter Name: ")
#         age = int(input("Enter Age: "))
#         gpa = float(input("Enter GPA: "))
#         data = struct.pack('i20sif', id_num, name.encode(), age, gpa)
#         file.write(data)
        
# print(f"{num_records} records have been written to records.bin")

# import struct

# with open("records.bin", "rb") as file:
    
#     data = file.read(struct.calcsize('i20sif'))
    
#     record = struct.unpack('i20sif', data)
    
#     record = (record[0], record[1].decode().strip('\x00'), record[2], record[3])
#     print(f"ID: {record[0]}, Name: {record[1]}, Age: {record[2]}, GPA: {record[3]}")

# import struct

# with open("records.bin", "rb") as file:
#     record_size = struct.calcsize('i20sif')
#     while True:
#         data = file.read(record_size)
#         if not data:
#             break
#         record = struct.unpack('i20sif', data)
#         record = (record[0], record[1].decode().strip('\x00'), record[2], record[3])
#         print(f"ID: {record[0]}, Name : {record[1]}, Age: {record[2]}, GPA: {record[3]}")

# import struct

# record_format = 'i20sif'
# record_size = struct.calcsize(record_format)

# with open('records.bin', 'rb') as file:
    
#     file.seek(record_size)
    
#     data = file.read(record_size)
#     record = struct.unpack(record_format, data)
    
#     record = (record[0], record[1].decode().strip('\x00'), record[2], record[3])
    
#     print(f"ID: {record[0]},Name : {record[1]},Age: {record[2]},GPA: {record[3]}")
    
# def example_w_plus_mode():
    
#     with open('example_w+.txt', 'w+') as file:
#         file.write("This is the first line in the file.\n")
#         file.write("This is the second line in the file.\n")
        
#         file.seek(0)
        
#         content = file.read()
#         print("Content of the file: ")
#         print(content)
        
# example_w_plus_mode()

# def example_a_plus_mode():
#     with open('example_a+.txt','a+') as file:
#         file.seek(0)
        
#         content = file.read()
#         print("Current content of the file:")
#         print(content)
        
#         file.write("Appending a new line at the end.\n")
        
#         file.seek(0)
#         updated_content = file.read()
#         print("\nUpdated content of the file:")
#         print(updated_content)
        
# example_a_plus_mode()