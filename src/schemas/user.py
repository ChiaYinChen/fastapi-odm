"""Schema for User."""
from typing import Annotated

from bson import ObjectId
from pydantic import BaseModel, EmailStr, Field, StringConstraints

from .common import ObjectIdPydanticAnnotation


class UserBase(BaseModel):
    """Base class with shared properties for user models."""
    email: EmailStr | None = None
    username: str | None = None
    is_active: bool | None = True
    is_superuser: bool | None = False


class UserCreate(UserBase):
    """Schema to receive data on user creation."""
    email: EmailStr
    username: Annotated[str, StringConstraints(min_length=3, max_length=64, strip_whitespace=True)]
    password: str = Field(..., min_length=6)


class UserUpdate(UserBase):
    """Schema to receive data on user update."""
    password: str | None = None


class User(UserBase):
    """Schema to return user data via API."""
    id: Annotated[ObjectId, ObjectIdPydanticAnnotation]
