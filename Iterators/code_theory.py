#!Iterator
"""An Iterator is a object that represent stream of data .it returns the data one element at a time"""
"""An iterator in Python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets. The Python iterators object is initialized using the iter() method. It uses the next() method for iteration."""

# !range => it gives a iterable object with an specific range(start,stop,step)
rng = range(10)
print(rng)
iterable_object = iter(rng)
print(next(iterable_object))
print(next(iterable_object))
print(next(iterable_object))
print(next(iterable_object))
print(next(iterable_object))
print(next(iterable_object))
print(next(iterable_object))
print(next(iterable_object))
print(next(iterable_object))
print(next(iterable_object))
# print(next(iterable_object))#when the iterating value is out then the stopiteration error raise.

# !here loop also follow the same step for iterating over a iterable object
for i in range(10, 20,2):
    print(i)

# ? enumerate => it adds a counter to an iterable and returns it as an enumerate object. This is useful for obtaining an indexed list.
li = list(range(10,40,2))
print(li)

enm_obj = enumerate(li)
print(enm_obj)

# print(next(enm_obj))
# print(next(enm_obj))
# print(next(enm_obj))
# print(next(enm_obj))
# print(next(enm_obj))

# it binds every single value with an index 
print("------------------------------------------")
for i,j in enumerate(li,start=1): #we can initialize from where the indexing should start...
    print(i,j)


# ! Custome Iterator :-

class custome_iterator:
    def __init__(self,end,start = 0,step = 1) -> None:
        self.start = start
        self.end = end
        self.step = step


    def __iter__(self):
        print("inside Iter")
        return self

    def __next__(self):
        print("inside next")
        if self.start < self.end:
            value = self.start
            self.start = self.start + self.step
            return value
        else :
            raise StopIteration()

first = custome_iterator(10)
print(first)
# print(next(first))
# print(next(first))
for i in first:
    print(i)
            