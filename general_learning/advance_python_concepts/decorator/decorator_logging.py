#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools

def log_functions(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling the function: {func.__name__}")
        print(f"Arguments: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@log_functions
def add(a, b=0):
    """Add two numbers."""
    return a + b

add(3, b=5)
