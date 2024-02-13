#!/usr/bin/env python3
"""Defining a class BasicAuth"""
from api.v1.auth.auth import Auth
from typing import Tuple, TypeVar
from models.user import User
import base64
import binascii


class BasicAuth(Auth):
    """Class BasicAuth that inherits from Auth"""
    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """extracts base64 auth header part"""
        if (authorization_header is None
                or type(authorization_header) != str
                or authorization_header[:6] != 'Basic '):
            return None
        else:
            return authorization_header[6:]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """returns a base64 auth header decoded"""
        if (base64_authorization_header is None
                or type(base64_authorization_header) != str):
            return None
        try:
            decode_base64 = base64.b64decode(base64_authorization_header)
        except binascii.Error:
            return None

        return decode_base64.decode('utf-8')

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """returns the email and the password of a user"""
        if (decoded_base64_authorization_header is None
                or type(decoded_base64_authorization_header) != str
                or ':' not in decoded_base64_authorization_header):
            return (None, None)

        email, password = decoded_base64_authorization_header.split(':')
        return (email, password)

    def user_object_from_credentials(
            self,
            user_email: str, user_pwd: str) -> TypeVar('User'):
        """returns a User object if exists in the db
        else None"""
        if (user_email is None
                or type(user_email) != str
                or user_pwd is None
                or type(user_pwd) != str):
            return None

        users_list = User.search({'email': user_email})
        if users_list:
            for users in users_list:
                if users.is_valid_password(user_pwd):
                    return users

        return None
