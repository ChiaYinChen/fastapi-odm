"""MongoDB connection."""
import logging
import traceback

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from ..core.config import settings
from ..models.user import User

logger = logging.getLogger(__name__)
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
        logger.info("Successfully connected to MongoDB")
    except Exception as exc:
        logger.error(f"Failed to connect to MongoDB. Error => {exc}")
        logger.info(traceback.format_exc())
