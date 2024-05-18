from pydantic_settings import BaseSettings

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent


class _Settings(BaseSettings):
    DATA_DIR: Path = Path("./data").resolve()
    MODEL_DIR: Path = Path("./models").resolve()
    RESULT_DIR: Path = Path("./results").resolve()


config = _Settings()
