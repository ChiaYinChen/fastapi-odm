"""Base constants."""
from enum import Enum


class BaseStrEnum(str, Enum):

    def __str__(self) -> str:
        return str(self.value)
