"""Router for user."""
from fastapi import APIRouter, Depends, status

from .. import repositories as crud
from .. import schemas
from ..consts.errors import CustomErrorCode
from ..depends.common import get_pagination_params, get_sorting_params
from ..handlers import exceptions as exc
from ..handlers.pagination import paginate
from ..models.user import User as UserModel
from ..schemas.responses import GenericResponse

router = APIRouter()


@router.get(
    "",
    response_model=GenericResponse[list[schemas.User]]
)
async def get_users(
    paging: schemas.PaginationParams = Depends(get_pagination_params),
    sorting: schemas.SortingParams = Depends(get_sorting_params)
) -> list[UserModel | None]:
    """
    Retrieve a list of users with optional pagination and sorting.
    """
    # TODO: if the number of users is zero, skip the pagination process
    queryset = await crud.user.get_all_instance()
    page_info, users = await paginate(queryset, paging_params=paging, sorting_params=sorting)
    return GenericResponse(data=users, paging=page_info)


@router.post(
    "",
    response_model=GenericResponse[schemas.User],
    status_code=status.HTTP_201_CREATED
)
async def create_user(user_in: schemas.UserCreate) -> UserModel:
    """
    Create a new user.
    """
    user_obj = await crud.user.get_by_email(email=user_in.email)
    if user_obj:
        raise exc.ConflictError(CustomErrorCode.ENTITY_CONFLICT, "Email already registered")
    users = await crud.user.create(obj_in=user_in)
    return GenericResponse(data=users)


@router.patch(
    "/{email}",
    response_model=GenericResponse[schemas.User]
)
async def update_user(email: str, user_in: schemas.UserUpdate) -> UserModel:
    """
    Update an existing user's information.
    """
    user_obj = await crud.user.get_by_email(email=email)
    if not user_obj:
        raise exc.NotFoundError(CustomErrorCode.ENTITY_NOT_FOUND, "User not found")
    users = await crud.user.update(db_obj=user_obj, obj_in=user_in)
    return GenericResponse(data=users)
