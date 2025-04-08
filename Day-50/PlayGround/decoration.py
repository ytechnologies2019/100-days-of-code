# ##Netstat
# def outer_function():
#     print('outer function')
#
#     def netstat_function():
#         print('inner function')
#
#     return netstat_function()
#
# inner_function = outer_function()
# print (inner_function)
#
# ##Function return from another function
import time
def decorator_function(function):
    def wrapper_function():
        time.sleep(5)
        function()
    return wrapper_function

@decorator_function
def say_hello():
    print ('Hello')
say_hello()

def say_bye():
    print ('Bye')
say_bye()