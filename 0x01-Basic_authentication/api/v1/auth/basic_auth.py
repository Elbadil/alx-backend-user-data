#!/usr/bin/env python3
"""Defining a class BasicAuth"""
from api.v1.auth.auth import Auth
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
