#!/usr/bin/env python3
"""Defining a Function filter_datum"""
from typing import List
import re
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]) -> None:
        super(RedactingFormatter, self).__init__()
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """returns a str representation of a LogRecord"""
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.msg, self.SEPARATOR)
        timestamp = self.formatTime(record, self.datefmt)
        return f"[HOLBERTON] {record.name} {record.levelname} {timestamp}: {record.msg}"


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """returns the log message obfuscated"""
    pattern = '|'.join(fields)
    return re.sub(f'({pattern})=([^{separator}]+)',
                  f'\\1={redaction}', message)
