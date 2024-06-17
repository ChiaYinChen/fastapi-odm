"""Log constants"""
from ..consts.base import BaseStrEnum


class LogLevel(BaseStrEnum):

    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"
