from typing import Final

from sqlalchemy import Column, Integer
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, declared_attr, sessionmaker

from app.core.config import settings

BD_URL: Final[str] = (
    f"postgresql+asyncpg://"
    f"{settings.db_user}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}"
)


class PreBase:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)
engine = create_async_engine(BD_URL)

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)


async def get_session():
    async with AsyncSessionLocal() as s:
        yield s
