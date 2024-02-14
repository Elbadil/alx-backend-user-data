#!/usr/bin/env python3
"""Defining a class SessionAuth"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """Class SessionAuth that inherits from Auth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates a session for a User"""
        if user_id is None or type(user_id) != str:
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns a user_id based on session_id given"""
        if session_id is None or type(session_id) != str:
            return None

        user_id = self.user_id_by_session_id.get(session_id)
        return user_id
