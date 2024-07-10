import os

"""
r: open an existing file for a read operation.
w: open an existing file for a write operation. If the file already contains some data, then it will be overridden but if the file is not present then it creates the file as well.
a:  open an existing file for append operation. It won’t override existing data.
r+:  To read and write data into the file. This mode does not override the existing data, but you can modify the data starting from the beginning of the file.
w+: To write and read data. It overwrites the previous file if one exists, it will truncate the file to zero length or create a file if it does not exist.
a+: To append and read data from the file. It won’t override existing data.

"""
with open("temp.txt","r+") as f:
    # print(f.read(10))#! also can pass the amount of words
    # print(f.read())
    # print(f.read())
    # print("----------------------")
    # print(f.readable())
    # print("----------------------")
    # print(f.readline(40)) #it just read one line at a time
    # print(f.readline()) #it just read one line at a time
    # print("----------------------")
    # print(f.readlines()) # it reads the raw string means include the \n and read all the data and return a list
    # print("----------------------")
    # !in file reading when we open a file there is a cursor which move so when you read the first line next time when you read the file it start from the previous position


    #? How to reset curosr
    print(f.read())
    print("------------------------")
    f.seek(0) # to set the cursor at begining
    print("------------------------")
    # print(f.read())

    # to set the end of the file 
    print("------------------------")
    f.seek(0, os.SEEK_END)
    print(f.readline())


# !working with csv files
# import csv

# # Writing to a CSV file
# with open('example.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Name', 'Age', 'City'])
#     writer.writerow(['Alice', 30, 'New York'])
#     writer.writerow(['Bob', 25, 'Los Angeles'])

# with open('example.csv', 'r') as file:
#     reader = csv.reader(file) #it returns an iterable object contains each line of file
#     print(reader)
#     for row in reader:
#         print(row)

# !read Binary files and writing in it

import os

# Writing to a binary file
with open('example.bin', 'wb') as file:
    file.write(b'\x00\x01\x02\x03\x04')
    print(f"Initial data written: {b'\x00\x01\x02\x03\x04'}")

# Appending to a binary file
with open('example.bin', 'ab') as file:
    file.write(b'\x05\x06\x07\x08\x09')
    print(f"Appended data: {b'\x05\x06\x07\x08\x09'}")

# Reading the binary file
with open('example.bin', 'rb') as file:
    data = file.read()
    print(f"Final data in file: {data}")

# !read Json file 
import json
with open ('data.json','w') as  file:
    data = {
    'Name': 'Alice',
    'Age': 30,
    'City': 'New York'
    }
    jsnodata = json.dump(data,file,indent=2)
    print(jsnodata)

with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)
    print(type(data))