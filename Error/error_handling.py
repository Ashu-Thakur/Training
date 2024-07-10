# there are two types Error:
# ! Syntax Error(Compile time error)
# ? Logical Error(Run Time Error)

# ! -------------------Types of In built Errors:--------------------------------

# ?IndexError- When the wrong index of a list is retrieved.
# ?AssertionError	It occurs when the assert statement fails
# ?AttributeError	It occurs when an attribute assignment is failed.
# ?ImportError	It occurs when an imported module is not found.
# ?KeyError	It occurs when the key of the dictionary is not found.
# ?NameError	It occurs when the variable is not defined.
# ?MemoryError	It occurs when a program runs out of memory.
# ?TypeError	It occurs when a function and operation are applied in an incorrect type.

# !Syntax Error
# Example: Missing a colon
# if True
#     print("Missing colon")

# !Indentation Error
# # Example: Incorrect indentation
# def my_function():
# print("Incorrect indentation")

# ! TypeError
# Example: Adding a string and an integer
# print("string" + 5)

# !ValueError: Raised when a function receives an argument of the correct type but inappropriate value.
# Example: Converting a string to an integer
# int("string")

#! ----------------------------------Raise-----------------------------------
# we can raise custome errors and raise any error when we want
# class CustomError(Exception):
#     """Custom exception for specific error conditions."""
#     def __init__(self, message, error_code):
#         super().__init__(message)
#         self.error_code = error_code

#     def __str__(self):
#         return f"{self.__class__.__name__}: {self.args[0]} (Error Code: {self.error_code})"

# def risky_function(value):
#     if value < 0:
#         raise CustomError("Negative value encountered", 1001)
#     elif value == 0:
#         raise CustomError("Zero value encountered", 1002)
#     else:
#         return f"Value is {value}"

# def main():
#     values = [10, 0, -3, 5]

#     for value in values:
#         try:
#             result = risky_function(value)
#             print(result)
#         except CustomError as e:
#             print(f"Handling custom error: {e}")
#         except Exception as e:
#             print(f"Handling general error: {e}")

# if __name__ == "__main__":
#     main()

#Error Logging
import logging

# Configure logging
logging.basicConfig(filename='Error/app.log', level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

try:
    # Code that may cause an error
    num = -1
    # result = 1 / 0
    if num < 0 :
        raise IndexError("This is out of Index")
except ZeroDivisionError as e:
    # Log the error
    logging.error(f"Error occurred: {e}")

except IndexError as E :
    logging.error(f"Error occurred: {E}")
