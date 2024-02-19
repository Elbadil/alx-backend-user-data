#!/usr/bin/python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from typing import Dict, Union

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Saves a user to the database"""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs: Dict[str, Union[str, int]]) -> User:
        """Finding a user based on the keyword arguments provided"""
        for key in kwargs.keys():
            if not hasattr(User, key):
                raise InvalidRequestError

        user = self.__session.query(User).filter_by(**kwargs).first()
        if user is None:
            raise NoResultFound

        return user

    def update_user(self, user_id: int,
                    **kwargs: Dict[str, Union[str, int]]) -> None:
        """Updates user's attribute values based on keyword
        arguments provided"""
        user = self.find_user_by(id=user_id)
        for key, val in kwargs.items():
            if not hasattr(User, key):
                raise ValueError
            setattr(user, key, val)

        self._session.commit()
