#!/usr/bin/env python3

def my_decorator(original_function):
    """Take a complete function"""
    def wrapper_function(*args, **kwargs):
        """Take args and kwargs"""
        print("This is before the function runs")
        result = original_function(*args, **kwargs)  
        print("This is after the function runs")
        return result 
    return wrapper_function

@my_decorator
def say_hello():
    print("hello")

if __name__ == "__main__":
    say_hello()
