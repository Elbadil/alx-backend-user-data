#!/usr/bin/env python3
"""Defining a Model Auth"""
import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


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
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_pwd = _hash_password(password)
            user = self._db.add_user(email, hashed_pwd)
            return user

        raise ValueError(f'User {user.email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        """checks if the password is valid for the users email"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        return bcrypt.checkpw(password.encode(), user.hashed_password)

    def create_session(self, email: str) -> str:
        """creates a session_id for a user"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id


def _generate_uuid():
    """returns a string representation of a new UUID"""
    return str(uuid.uuid4())
