#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools

def validate_email(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        user = kwargs.get("user", {})
        email = user.get("email", "")
        if "@" in email and "." in email:
            return func(*args, **kwargs)
        else:
            raise ValueError("❌ Invalid email address")
    return wrapper


def validate_password(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        user = kwargs.get("user", {})
        password = user.get("password", "")
        if len(password) >= 8:
            return func(*args, **kwargs)
        else:
            raise ValueError("❌ Password must be at least 8 characters long")
    return wrapper

@validate_email
@validate_password
def user_info(user):
    return user

# ✅ Try it
if __name__ == "__main__":
    try:
        result = user_info(user={"name": "John Doe", "email": "humairmunir@gmail.com" , "password": "12345678"})
        print(result)
    except ValueError as e:
        print(e)
