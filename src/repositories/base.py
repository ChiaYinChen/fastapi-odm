"""Base class for CRUD operations on database models."""
from datetime import datetime
from typing import Any, Generic, Type, TypeVar, Union

from beanie import Document
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

ModelType = TypeVar("ModelType", bound=Document)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """
    Provides generic CRUD (Create, Read, Update, Delete) operations for a given model.

    Parameters:
        model: A Document model class
        schema: A Pydantic model (schema) class

    Methods:
        get(id): Retrieve an instance based on its ID.
        get_multi(skip, limit): Retrieve multiple instances based on skip and limit.
        create(obj_in): Create a new instance from a schema.
        update(db_obj, obj_in): Update an existing instance.
        remove(db_obj): Remove an existing instance.
    """

    def __init__(self, model: Type[ModelType]):
        """
        Initializes the CRUD object with a model class.

        Args:
            model (Type[ModelType]): The Document model class to perform operations on.
        """
        self.model = model

    async def get(self, id: Any) -> ModelType | None:
        """Retrieve a single instance by its ID."""
        return await self.model.get(id)

    async def get_multi(self, skip: int = 0, limit: int = 5000) -> list[ModelType | None]:
        """
        Retrieve a list of instances, with pagination support.

        Args:
            skip (int): Number of instances to skip.
            limit (int): Maximum number of instances to return.

        Returns:
            A list of model instances.
        """
        return (
            await self.model.find()
            .skip(skip)
            .limit(limit)
            .to_list()
        )

    async def create(self, obj_in: CreateSchemaType) -> ModelType:
        """
        Create a new model instance based on schema data.

        Args:
            obj_in (CreateSchemaType): Schema containing the data for the new instance.

        Returns:
            The newly created model instance.
        """
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        return await db_obj.create()

    async def update(
        self,
        db_obj: ModelType,
        obj_in: Union[UpdateSchemaType, dict[str, Any]]
    ) -> ModelType:
        """
        Update an existing model instance.

        Args:
            db_obj (ModelType): The instance to be updated.
            obj_in (Union[UpdateSchemaType, dict]): Schema or dictionary with updated values.

        Returns:
            The updated model instance.
        """
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
            if field == "updated_at":
                breakpoint()
                setattr(db_obj, field, datetime.now())
        await db_obj.save()
        return db_obj

    async def remove(self, db_obj: ModelType) -> ModelType:
        """
        Remove an existing model instance.

        Args:
            db_obj (ModelType): The instance to be removed.

        Returns:
            The removed (deleted) model instance.
        """
        await db_obj.delete()
        return db_obj
