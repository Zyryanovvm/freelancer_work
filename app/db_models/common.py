from sqlalchemy import Column, String

from app.core.db import Base


class Categories(Base):
    name = Column(String(100), unique=True, nullable=False)


class Languages(Base):
    name = Column(String(100), unique=True, nullable=False)


class Statuses(Base):
    name = Column(String(100), unique=True, nullable=False)
