"""User document."""
from typing import Annotated

from beanie import Indexed
from pydantic import EmailStr

from ..models.base import BaseDocument


class User(BaseDocument):

    email: Annotated[EmailStr, Indexed(unique=True)]
    username: Annotated[str, Indexed()]
    password: str
    is_active: bool = True
    is_superuser: bool = False

    class Settings:
        name = "USERS"
