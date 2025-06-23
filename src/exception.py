import sys 


def error_message_detail(error,error_detail:sys): #Purpose: This defines a helper function. Its job is to take a raw Python exception (error) and the sys module context (error_detail) and format them into a human-readable error message.
    _,_,exc_tb=error_detail.exc_info()  
    file_name=exc_tb.tb_frame.f_code.co_filename    
    error_message="error occured in python script name [{0}] line number [{1}] error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    return error_message


class custom_exception(Exception):
    def __init__(self,error_message,error_detail:sys):
        super.__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
   


#explanation of this above code:-
# line 1:- import sys
# Purpose: Imports the sys module. As we discussed, sys provides access to system-specific parameters and functions, which are critical here for getting detailed error information.

# Line 3: def error_message_detail(error, error_detail:sys):
# Purpose: This defines a helper function. Its job is to take a raw Python exception (error) and the sys module context (error_detail) and format them into a human-readable error message.
# error: This parameter will be the actual exception object that was caught (e.g., ZeroDivisionError('division by zero')).
# error_detail:sys: This parameter is type-hinted as sys. This isn't strictly enforcing sys to be passed, but it's a strong hint that the function expects sys itself (or an object that provides exc_info() like sys does) so it can access detailed traceback information.

# Line 4: _, _, exc_tb = error_detail.exc_info()
# Purpose: This is the core line for extracting error details.
# error_detail.exc_info(): When an exception occurs, sys.exc_info() (or error_detail.exc_info() in this context, assuming error_detail is sys) returns a tuple of three values:
# type: The exception class (e.g., <class 'ZeroDivisionError'>).
# value: The exception instance (e.g., ZeroDivisionError('division by zero')).
# traceback: A traceback object, which contains information about where the exception occurred (file, line number, function calls leading up to it).
# _, _, exc_tb = ...: The _ (underscore) is a convention in Python to indicate a variable that you don't intend to use. Here, we're only interested in the third element of the tuple, which is the traceback object (exc_tb).

# Line 5: file_name = exc_tb.tb_frame.f_code.co_filename
# Purpose: Extracts the name of the file where the error occurred.
# exc_tb: The traceback object.
# .tb_frame: The frame object for the current stack level in the traceback. A "frame" holds information about a function call (local variables, code being executed, etc.).
# .f_code: The code object being executed in that frame. A "code object" contains immutable information about a piece of Python code.
# .co_filename: The name of the file in which this code object was defined.

# Line 6: line_number = exc_tb.tb_lineno
# Purpose: Extracts the line number within the file_name where the error occurred.
# .tb_lineno: The current line number in the traceback frame.

# Lines 7-8: error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(file_name, line_number, str(error))
# Purpose: Constructs the final, detailed error message string.
# "{0}] ... [{1}] ... [{2}]".format(...): This is string formatting.
# {0} will be replaced by file_name.
# {1} will be replaced by line_number.
# {2} will be replaced by str(error) (which is the string representation of the actual exception, like "division by zero").
# This line creates a clear, informative message like: "Error occurred in python script name [my_script.py] line number [15] error message [division by zero]".
# 
# Line 10: return error_message
# Purpose: Returns the meticulously crafted error message.

# Line 12: class CustomException(Exception):
# Purpose: Defines a new custom exception class named CustomException.
# (Exception): This is crucial! It means CustomException inherits from Python's built-in Exception class. By inheriting from Exception, CustomException behaves like a standard exception and can be caught using try...except blocks.

# Line 13: def __init__(self, error_message, error_detail:sys):
# Purpose: This is the constructor method for your CustomException class. It gets called automatically when you create a new instance of CustomException (e.g., raise CustomException("Something went wrong", sys)).
# self: Refers to the instance of the CustomException being created.
# error_message: The message you want to associate with this specific custom exception (e.g., "Data Ingestion Failed"). This will be passed to the error_message_detail function.
# error_detail:sys: Again, type-hinted to expect the sys module, which will be used to extract the detailed traceback.

# Line 14: super().__init__(error_message)
# Purpose: Calls the constructor of the parent class (Exception).
# super(): A special function that allows you to call methods from the parent class.
# __init__(error_message): The Exception class's constructor takes a message as an argument. By passing error_message here, you ensure that your CustomException also has a standard message property that can be accessed like e.args[0] if needed, and it allows it to be printed directly.

# Line 15: self.error_message = error_message_detail(error_message, error_detail=error_detail)
# Purpose: This is where the magic happens! It calls the error_message_detail function we defined earlier.
# It passes the original error_message you provided when raising the CustomException (e.g., "Data Ingestion Failed") as the first argument, and the sys module as the error_detail.
# The result (the detailed formatted string like "Error occurred in python script name [...]") is then stored as an attribute self.error_message within your CustomException instance.

# Line 17: def __str__(self):
# Purpose: This is a "dunder" (double underscore) method that defines what happens when you try to convert an object of CustomException to a string (e.g., when you print(my_custom_exception_instance) or str(my_custom_exception_instance)).
# self: The instance of the CustomException.

# Line 18: return self.error_message
# Purpose: When you print or cast your CustomException object to a string, it will return the detailed self.error_message that was generated in the __init__ method, which contains the file name, line number, and the original error message.

# How would you use this CustomException?
# Python
# # In some other file, e.g., 'your_script.py'
# import sys
# from exception import CustomException # Assuming exception.py is in the same directory or accessible

# def divide(a, b):
#     try:
#         return a / b
#     except Exception as e: # Catch any built-in exception
#         # Now raise your custom exception, passing the original error and sys module
#         raise CustomException(f"Error during division operation: {e}", sys)


# if __name__ == "__main__":
#     try:
#         result = divide(10, 0)
#         print(f"Result: {result}")
#     except CustomException as ce: # Catch your custom exception
#         print(f"Caught Custom Exception: {ce}")
#         # You could also log this 'ce' to a file here
#     except Exception as e:
#         print(f"Caught generic exception: {e}")

# When you run your_script.py and division by zero occurs, the output would look something like:

# Caught Custom Exception: Error occurred in python script name [your_script.py] line number [9] error message [Error during division operation: division by zero]
# This is much more informative than just division by zero, as it tells you exactly where in your code the issue originated!

# I hope this detailed breakdown makes exception.py much clearer! It's a powerful pattern for creating more helpful debugging and logging messages in your ML projects.
