#!/usr/bin/env python3
"""Defining a Function filter_datum"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """returns the log message obfuscated"""
    for msg in message.split(separator):
        if msg.split('=')[0] in fields:
            message = re.sub(f'{msg.split("=")[1]}', redaction, message)
    return message
