#!/usr/bin/env python3
"""Defining a class BasicAuth"""
from api.v1.auth.auth import Auth


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
