"""Error code constants."""
from enum import Enum


class CustomErrorCode(str, Enum):

    # validation errors
    VALIDATE_ERROR = "0000"                         # General validation error
