# ?Decorators :
def decorator(func):
    def wrapper(*args, **kwargs):
        print(*args,args)
        print(kwargs,**kwargs)
        print("Hello By before function calling")
        returned_value = func(*args, **kwargs)
        print("After function calling")
        return returned_value
    return wrapper

@decorator
# internally this looks like decorator(Square(*args))
def Square(*args, **kwargs):
    print(args, kwargs)
    return [i**2 for i in args]

li = Square(2, 4, 6, 8, 10, 12, 14, 16, 18)
print(li)


# mutliple decorators
# code for testing decorator chaining 
print("---------------------------------")
def decor1(func):
    print("deor1 outer")
    def inner(x):
        print("inside decor1",func, x)
        flag = func(x)
        if flag:
            print("Prime Number")
        return flag
    return inner

def decor(func):
    print("decor outer")
    def inner(x):
        print("inside Decor",func,x)
        return func(x)
    return inner

@decor1
@decor
def num(x):
    flag = True
    for i in range(2, x):
        if x % i == 0:
            flag = False
            break
    return flag

num(11) 
#flow to this function is decor1(decor(num))
# decor1(func = decor.inner)
# decor1.inner()
# that's why the flow of print of  this decorator is
# ? decor outer
# ? deor1 outer
# ? inside decor1 <function decor.<locals>.inner at 0x7f4b14433940> 11
# ? inside Decor <function num at 0x7f4b14433f70> 11
# ? Prime Number
num(12)

# !custome decorater with perameters
import functools

# Step 1: Define the decorator factory
def conditional_log_decorator(condition):
    def log_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """
            this is wrapper function
            """
            if condition:
                print(f"Arguments: args={args}, kwargs={kwargs}")
            result = func(*args, **kwargs)
            if condition:
                print(f"Return value: {result}")
            return result
        return wrapper
    return log_decorator

# Step 2: Define the function
@conditional_log_decorator(condition=False)  # Change to False to disable logging
def multiply_numbers(a, b):
    """
    this function mainly for multiplying the two numbers
    """
    return a * b

# Step 3: Apply the decorator and test the function
result = multiply_numbers(3, 4)
print(f"Result: {result}")
print(multiply_numbers.__name__)
print(multiply_numbers.__doc__)
# Flow for this code :-
"""
@conditional_log_decorator(condition=False): this function is called and return a another decorator "log_decorator"
now log_decorator this takes the function as perameter and then it returns a wrapper function
now this function called and we get the output
"""
#!  @functools.wraps(func) this line save the meta info about the callback function otherwise it will lose it's meta data
 
# ?Practice code
import time
import functools

def Time(repeats=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            total_time = 0
            for _ in range(repeats):
                start = time.time()
                result = func(*args, **kwargs)
                end = time.time()
                total_time += end - start
            average_time = total_time / repeats
            return result, average_time
        return wrapper
    return decorator

@Time(repeats=10)
def PrimeNumber_non_optimized(x):
    li = list()
    for i in range(2, x):
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = not flag
                break
        if flag:
            li.append(i)
    return li

@Time(repeats=10)
def PrimeNumber(x):
    li = list()
    for i in range(2, x):
        flag = True
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                flag = not flag
                break
        if flag:
            li.append(i)
    return li

result1, time1 = PrimeNumber_non_optimized(999)
result2, time2 = PrimeNumber(999)
print(f"First Result takes {time1:.6f} seconds for having {len(result1)} prime numbers.")
print(f"Second Result takes {time2:.6f} seconds for having {len(result2)} prime numbers.")


