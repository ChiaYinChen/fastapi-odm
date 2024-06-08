"""User document."""
from typing import Annotated

from beanie import Indexed
from pydantic import EmailStr, Field

from ..models.base import BaseDocument


class User(BaseDocument):

    email: Annotated[EmailStr, Indexed(unique=True)]
    username: Annotated[str, Indexed()]
    hashed_password: str = Field(alias="password")
    is_active: bool = True
    is_superuser: bool = False

    class Settings:
        name = "USERS"
