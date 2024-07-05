"""!Data Types : Every value has a datatype, and variables can hold values. Python is a powerfully composed language; consequently, we don't have to characterize the sort of variable while announcing it. The interpreter binds the value implicitly to its type."""

#! ___________We did not specify the type of the variable a, which has the value five from an integer.__________

#?Python has the following data types built-in by default, in these categories:

#!Numeric Types :int, float, complex

#!Text Type:str

#!Sequence Types:list, tuple, range

#!Mapping Type:	dict

#!Set Types: set, frozenset

#!Boolean Type:	bool

#!Binary Types:	bytes, bytearray, memoryview

#!None Type: NoneType

# !--------------------------------------------------------------------------------------------
# !__________Numeric Types__________

# ? Integer Numbers : Represents whole numbers without a fractional part.
a = 5

print(type(a))

# can store as big as can at a certain limit 
# a = 12222222222222222222222222222222222333333333333333333333333333332222222222223
# print(type(a),a)
print("_________________________________________________________________________________________")

a = 1234567890123456789012345678901234567890
b = 9876543210987654321098765432109876543210
c = a * b
print(c)
print(type(c))
print("_________________________________________________________________________________________")

# for big number we can use underscore
number = 1_000_000_0000
print(number, type(number))
print("_________________________________________________________________________________________")


# print(248**1000)

# we can't print a number above 4300 digit 
# print(2345 ** 10000)
# for achieve that we need to use the methode


# Prefix	Representation with respect to their Base
# ? 0b or 0B (Zero + b or B)	Binary	2
# ? 0o or 0O (Zero + o or O)	Octal	8
# ? 0x or 0X (Zero + x or X)	Hexadecimal	16

# print("_________________________________________________________________________________________")
# print(0b110)
# print(0o110)
# print(0x110)
# print("All types would be Int")
print("_________________________________________________________________________________________")
# num = 10.5
# print(num.as_integer_ratio())#denometer will always positive


# num = 29  # Binary: 11101
# length = num.bit_length()
# print(length)

# count = num.bit_count()#counting the 1 accurance in binary representation

# print(count)

# print("converting into binary :",num.to_bytes())
# num = 14.6
# print("finding is it a integer or not :",num.is_integer())
# print("10.00 is return ",10.00.is_integer())

# ?there is built in methode int() to convert the all other types of interger into number 
# print("int(10.50)",int(10.50))
#print("int(10+2j)",int(10+2j))#we can't convert a complex into integer

print(int("10",base=2))
print(int("10",base=8))
print(int("10",base=10))

print("for converting that complex to int",10 + 2j.real)

# !--------------------------------------------------------
# ?Floating Number :  Represents a real number with a fractional part.

floatint_number = 10.55
print(floatint_number,type(floatint_number))

f_number = .4e5 #e represent how manay number would be lies before decimal point like 5 values lies before point 40000.0
print(f_number)

#!1.8x10.308 if a number goes bigger than its range than the number will represent in inf str
print(-.75e308)

G = 6.67430e-11

print(G.as_integer_ratio())
# (1290997375656627, 19342813113834066795298816)

print("without passing any value to the float function",float())
print(float(10))
print(float("10"))
# print(float("ten"))

# !complex numbers 
cmpx = 1 + 2j
print(cmpx,type(cmpx))

cmpx = 2j
print(cmpx)

# cmpx = 1 + j # got error
# print(cmpx)

cmpx = 2 + 2j
cmpx2 = 4 + 4j
print( f"{cmpx} + {cmpx2} = {cmpx + cmpx2}") 
print( f"{cmpx} - {cmpx2} = {cmpx - cmpx2}") 
#this is performing by
#  a + bj/ b + dj * b-dj / b-dj 
print( f"{cmpx} * {cmpx2} = {cmpx * cmpx2}") 
print( f"{cmpx2} / {cmpx} = {cmpx2 / cmpx}") 
# print( f"{cmpx2} % {cmpx} = {cmpx2 % cmpx}") #we can't applly this on complex operators

print("complex litralse _________________________")

print(complex())
print(complex(12))
print(complex(2,6))
print(complex(2.5, 4.5))


# !------------------------

# ?Text Type:The sequence of characters in the quotation marks can be used to describe the string.
string = "The Python Language"
string2 = "Popular in the World"
print(string +" " +string2)

print(string*3)
print (string[0:2:4]) #printing first two character using slice operator    
print (string[::-1]) #reversing the string  
print (string[4]) #printing 4th character of the string   
num =12.888888
print(f"Hello How Are You Old?{num:.2f}")
print("{}{}{}".format("Hello","Good","Morning"))
print(string.count('a'))

print('P' in string)
print('x' in string)
print('P' not in string)
print('x'not in string)
string = "HelloWorldz"
# it will find min and max according to the ascii value
print(":",min(string))
print(":",max(string))

# joint a list of number with an character
a = [1, 2, 3, 4 ,5]
print("-".join([str(i)for i in a]))
print("--------------------------------------")
class Student:
    def __init__(self, name, RNum) -> None:
        self.name = name
        self.Roll_number  = RNum

    def __str__(self) -> str:
        print("Hii")
        return f"{self.name} and it's RollNumber is {self.Roll_number}"
    
    def __repr__(self) -> str:
        return f"Student(name={self.name!r}, Roll_number={self.Roll_number!r})"
    
std1 = Student("Rahul", 1001)
print(std1)
str(std1)
print(std1.__repr__())

# !-----------------------------------------------------------Sequence Types-----------------------------------------------
#!Sequence Types:list, tuple, range
# ?-----------------------------------------------------------List---------------------------------------------------------

#? List :  it is ordered and mutable data structure,that can contain items of different types.on each index it store the object refrence address

# Two ways to crate array
my_list = [1, "hello", 3.14]
li2 = list(range(10))
print(my_list)
print(li2)

print("-------------------------------------")
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
my_list2 = my_list # but refereing same memory refrences
my_list.pop() # from both list the last element will be removed 
print(my_list)
print(my_list2)

# to avoid this let's use shallow copy and deep copy
import copy

shallow_list_copy = copy.copy(my_list)
print("After Making An Shallow Copy of The list :",shallow_list_copy)
shallow_list_copy.append(10)
print("after updating the shallow copy",shallow_list_copy)
print("main list",my_list)

# but if have nested objects then it referes to the same
new_list = [1,2,[3, 5, 6]]
copy_of_list = copy.copy(new_list)
print("before:",new_list,"\n",copy_of_list)
copy_of_list[2][1:] = (4,5)
print("After updating the copy :",copy_of_list) 
print("After updating the Orignal :",new_list) 

# now Deep copy
print("Now Deep Copy ----------------------")
new_list = [1,2,[3, 5, 6]]
deep_copy = copy.deepcopy(new_list)
print("before:",new_list,"\n",deep_copy)
deep_copy[2][1:] =(4,5)
print("After updating the copy :",deep_copy) 
print("After updating the Orignal :",new_list) 

# shallow copy by copy methode
new_list = [1,2,[3, 5, 6]]
new_copy = new_list.copy()
new_copy.append(11)
print(new_list is new_copy)
print(new_list[2] is new_copy[2])
print(new_copy,new_list)

# Add
li =[1,2,3]
# append add all element at the end of list with the same data structure as we passed
li.append((2,3))
li.append([2,3])
# while extend add only element,it requires a itreable object
li.extend([1,2,3,4])
li.extend((1,2,3,4))
print(li)

# Update,delete
li.pop(-1)#taking index
li.remove(2)
print(li)

# reversed
print("-------------------")
li.reverse()
print(li)
# short
li = [5,3,2,9,11,1999,99,999,2,1,55,2,33,44.5]
li.sort()
li.sort(reverse=True)
# li.sort(key=lambda x:len(str(x)),reverse=True)
# print(li)
print(li.count(2))
print(li)

# ord function
# print(map(lambda x:ord(x)))

# ?Reduce
from functools import reduce
ans = reduce(lambda x,y:x+y,li)
print(ans)
print(sum(li))

# ?Map
string = "Hello world"
print(list(map(ord,string)))
print(list(map(lambda x: x**2, li)))

# ?Filter
from functools import reduce
from itertools import accumulate

# Sample list
numbers = [1, 2, 3, 4, 5]
chars = ['a', 'b', 'c']
words = ["apple", "banana", "cherry"]
boolean_list = [True, True, False]

# sum(): Sum up the numbers in the list
sum_result = sum(numbers)
print("sum:", sum_result)



# min(): 
min_value = min(numbers)
print("min:", min_value)

# all():
all_true = all(boolean_list)
print("all:", all_true)

# any():
any_true = any(boolean_list)
print("any:", any_true)


# enumerate(): Returns enumerate object of the list
enumerated_list = list(enumerate(words))
print("enumerate:", enumerated_list)

accumulated_sum = list(accumulate(numbers, lambda x, y: x + y))
print("accumulate (summation):", accumulated_sum)


filtered_list = list(filter(lambda x: x % 2 == 0, numbers))
print("filter (even numbers):", filtered_list)

# !tuple : It's immutable and ordered strucutre
tup = (1,2,3)
tup2 = (1,) # for single element we should pass one comma
print(type(tup))
print(type(tup2))

# slicing
print(tup[:2])
print(tup[-1])
# indexing
tup =((1,2),(3,4))
print(tup[0][0], tup[1][0])
# repeating
print(tup*3)

print((tup[0][0],tup[1][0]))
# tuple by list
print(tuple(list(range(10))))


#? range
print(range(10))
print(range(10, 2))
print(range(10, 2, -1))

#!--------------------------Mapping Object--------------------------------------------
dic = {"Name":"Ashutosh Thakur","class":12,"Roll_Number":1001}
dic2 = {"Name":"Vinay","class":10,"Roll_Number":1002}
