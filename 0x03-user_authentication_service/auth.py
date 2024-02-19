#!/usr/bin/env python3
"""Defining a Model Auth"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Returns a password hashed in bytes"""
    en_password = password.encode()
    hashed_pwd = bcrypt.hashpw(en_password, bcrypt.gensalt())
    return hashed_pwd
