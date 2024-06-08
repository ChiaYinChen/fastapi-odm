"""MongoDB connection."""
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from ..core.config import settings
from ..models.user import User

client = AsyncIOMotorClient(settings.MONGO_URI)


async def start_async_mongodb() -> None:
    """Start beanie when process started."""
    try:
        await init_beanie(
            database=getattr(client, settings.MONGO_DB),
            document_models=[
                User,
            ],
        )
        print("Successfully connected to MongoDB")
    except Exception as exc:
        print(f"Failed to connect to MongoDB. error={exc}")
