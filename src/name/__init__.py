from pydantic_settings import BaseSettings

from pathlib import Path


class _Settings(BaseSettings):
    DATA_DIR: Path = Path("./data").resolve()
    MODEL_DIR: Path = Path("./models").resolve()
    RESULT_DIR: Path = Path("./results").resolve()


config = _Settings()
