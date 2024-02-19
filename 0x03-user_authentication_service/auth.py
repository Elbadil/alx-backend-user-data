#!/usr/bin/env python3
"""Defining a Model Auth"""
import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Returns a password hashed in bytes"""
    en_password = password.encode()
    hashed_pwd = bcrypt.hashpw(en_password, bcrypt.gensalt())
    return hashed_pwd


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a new user in the db if not already exists"""
        user = self._db._session.query(User).filter_by(email=email).first()
        if user:
            raise ValueError(f'User {user.email} already exists')

        hashed_pwd = _hash_password(password)
        user = self._db.add_user(email, hashed_pwd)

        return user
