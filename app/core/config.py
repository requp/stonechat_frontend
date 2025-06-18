from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
        Configuration settings for the application, loaded from environment variables or a .env file.

        Attributes:
            MODE (str): The application mode (e.g., development, production).
            UVICORN_PORT (int): The port number on which the Uvicorn server runs.
            UVICORN_HOST (str): The host address for the Uvicorn server.
            PROD_HOST (str): The host address for the production server.
            PROD_PORT (int): The port number for the production server
    """

    MODE: str
    UVICORN_PORT: int
    UVICORN_HOST: str
    PROD_HOST: str
    PROD_PORT: int
    BACKEND_API_V1_URL: str

    @property
    def PROD_URL(self) -> str:
        return f"http://{self.PROD_HOST}:{self.PROD_PORT}"

    @property
    def BACKEND_AUTH_GOOGLE_URL(self) -> str:
        return f"{self.BACKEND_API_V1_URL}/login/google"

    model_config = SettingsConfigDict(
        env_file=f"{Path(__file__).resolve().parent.parent.parent}/.env",
        extra="allow"
    )

settings = Settings()