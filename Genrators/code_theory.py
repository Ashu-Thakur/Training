#!-----------------------Genrators-------------------------------------------
"""generator functions are a special kind of function that return a lazy iterator. These are objects that you can loop over like a list. However, unlike lists, lazy iterators do not store their contents in memory"""

# def infinite_sequence():
#     num = 0
#     while True:
#         yield num
#         num += 1

# gen = infinite_sequence()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

"""yield indicates where a value is sent back to the caller, but unlike return, you don’t exit the function afterward.
Instead, the state of the function is remembered. That way, when next() is called on a generator object , the previously yielded variable num is incremented, and then yielded again."""

# !----------------------Febbonacci Genrator---------------------------------

# def feb_genratore():
#     a = 0
#     b = 1
#     while True :
#         yield a
#         a, b = b ,a + b
        
# gen = feb_genratore()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# Reading file with genrators
import csv
with open("/home/developer/Downloads/customers-100.csv",'r') as f:
    file = csv.reader(f)
    gen = (s for s in file)
    coloum_name = next(gen)
    for line in gen:
        print(line)
    
