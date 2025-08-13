from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import Base
from app.schemas.common import Common


async def create_common_obj(
    table: Base, instance: Common, session: AsyncSession
) -> Base:
    """
    Создание объекта в базовой таблице БД
    """
    db_obj = table(**instance.model_dump())
    session.add(db_obj)
    await session.commit()
    await session.refresh(db_obj)
    return db_obj


def get_exist_criteria_by_name(table: Base, name: str):
    """
    Получение критерия существования
    объекта с заданным именем в базовых таблицах
    """
    return select(table).where(table.name == name).exists()


async def check_exist(exist_criteria, session: AsyncSession) -> bool:
    """
    Проверка существования объекта в
    БД
    """
    check_result = await session.execute(select(True).where(exist_criteria))
    return check_result.scalars().first()


async def get_all_objects(table: Base, session: AsyncSession):
    """
    Получение всех объекто в БД
    из базовой таблицы
    """
    result = await session.execute(select(table))
    return result.scalars().all()
