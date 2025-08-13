from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_session
from app.crud.common import (check_exist, create_common_obj,
                             get_exist_criteria_by_name)
from app.db_models.common import Categories, Languages, Statuses
from app.schemas.common import (CategoriesCreate, CommonDB, LanguagesCreate,
                                StatusesCreate)

router = APIRouter()


@router.post(
    "/category/",
    tags=["Admin methods"],
    summary="Добавление категорий заказов",
    response_model=CommonDB,
    response_model_exclude_none=True,
)
async def create_category(
    category: CategoriesCreate, session: AsyncSession = Depends(get_session)
):
    exist_criteria = get_exist_criteria_by_name(Categories, category.name)
    if await check_exist(exist_criteria, session):
        raise HTTPException(
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
            detail=f"Категория {category.name} уже существует",
        )
    db_obj = await create_common_obj(Categories, category, session)
    return db_obj


@router.post(
    "/language/",
    tags=["Admin methods"],
    summary="Добавление языка программирования",
    response_model=CommonDB,
)
async def create_language(
    language: LanguagesCreate, session: AsyncSession = Depends(get_session)
):
    exist_criteria = get_exist_criteria_by_name(Languages, language.name)
    if await check_exist(exist_criteria, session):
        raise HTTPException(
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
            detail=f"Язык {language.name} уже существует",
        )
    db_obj = await create_common_obj(Languages, language, session)
    return db_obj


@router.post(
    "/status/",
    tags=["Admin methods"],
    summary="Добавление статусов заказов",
    response_model=CommonDB,
)
async def create_status(
    status: StatusesCreate, session: AsyncSession = Depends(get_session)
):
    exist_criteria = get_exist_criteria_by_name(Statuses, status.name)
    if await check_exist(exist_criteria, session):
        raise HTTPException(
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
            detail=f"Статус {status.name} уже существует",
        )
    db_obj = await create_common_obj(Statuses, status, session)
    return db_obj
