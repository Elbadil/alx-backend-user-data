#!/usr/bin/env python3
"""Defining a function hash_password"""
import bcrypt
from typing import ByteString


def hash_password(password: str) -> ByteString:
    """returns a hashed password"""
    b_password = password.encode()
    hashed_pswd = bcrypt.hashpw(b_password, bcrypt.gensalt())
    return hashed_pswd
