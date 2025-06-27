#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author : Humair Munir
@brief: This module uses decorators for logging and security.
@version: 1.0
@license: MIT License
"""

import functools
import time

# ✅ Timing decorator


def timing(func):
    @functools.wraps(func)
    def wrapper(*args , **kwargs):
        print(f"Calculating time for Function {func.__name__}")
        start_time = time.time()
        results = func(*args, **kwargs)
        end_time = time.time()
        total_time = end_time - start_time 
        print(f"Time taken for {func.__name__} is : {total_time:.8f} seconds")
        return results
    return wrapper

# ✅ Logging Decorator
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"📋 Calling the function: {func.__name__}")
        print(f"➡️  Arguments: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"✅ Result: {result}")
        return result
    return wrapper

# ✅ Security Decorator
def security(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        user = kwargs.get("user", {})
        if user.get("is_auth") is True:
            print("🔐 Access granted. Fetching the database...")
            return func(*args, **kwargs)
        else:
            print("🚫 Access denied. You are not authorized.")
            return None
    return wrapper

# ✅ Sample info display function (renamed)
def show_info(name, age):
    return f"Name: {name}, Age: {age}"


# ✅ Example usage of the timing decorator
@timing
# ✅ Logged function
@log
# ✅ Secured function
@security
def fetch_db(**kwargs):
    time.sleep(1)
    return {"data": "Sample DB content", "user": kwargs.get("user")}

# ✅ Example usage
if __name__ == "__main__":
    print("\n🧪 Try 1: Security - Unauthorized")
    user_unauth = {"name": "Guest", "is_auth": False}
    fetch_db(user=user_unauth)

    print("\n🧪 Try 2: Security - Authorized")
    user_auth = {"name": "Humair", "is_auth": True}
    fetch_db(user=user_auth)
