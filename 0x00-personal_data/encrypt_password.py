#!/usr/bin/env python3
"""Defining a function hash_password"""
import bcrypt


def hash_password(password: str) -> bytes:
    """returns a hashed password"""
    b_password = password.encode()
    hashed_pswd = bcrypt.hashpw(b_password, bcrypt.gensalt())
    return hashed_pswd
