import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DEFAULT_DATABASE_URL = "postgresql+psycopg://app:app@localhost:5432/app"


def database_url() -> str:
    return os.environ.get("DATABASE_URL", DEFAULT_DATABASE_URL)


def make_engine(url: str | None = None):
    return create_engine(url or database_url())


engine = make_engine()
Session = sessionmaker(bind=engine)
