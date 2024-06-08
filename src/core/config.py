"""Settings."""
from pydantic import model_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # Application
    API_PREFIX: str = "/api"

    # MongoDB
    MONGO_USERNAME: str
    MONGO_PASSWORD: str
    MONGO_HOST: str = "mongodb"
    MONGO_PORT: int = 27017
    MONGO_DB: str
    MONGO_URI: str | None = None

    @model_validator(mode="after")
    @classmethod
    def validate_mongo_uri(cls, values):
        if isinstance(values.MONGO_URI, str):
            return values
        values.MONGO_URI = "mongodb://{username}:{password}@{host}:{port}".format(
            username=values.MONGO_USERNAME,
            password=values.MONGO_PASSWORD,
            host=values.MONGO_HOST,
            port=values.MONGO_PORT,
        )
        return values

    class Config:
        case_sensitive = True


settings = Settings()
