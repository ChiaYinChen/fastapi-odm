"""CRUD for user."""
from ..models.user import User as UserModel
from ..repositories.base import CRUDBase
from ..schemas.user import UserCreate, UserUpdate


class CRUDUser(CRUDBase[UserModel, UserCreate, UserUpdate]):
    """CRUD operations for user model."""

    async def get_by_username(self, username: str) -> UserModel | None:
        """Retrieve a user by their username."""
        return await UserModel.find_one(UserModel.username == username)


user = CRUDUser(UserModel)
