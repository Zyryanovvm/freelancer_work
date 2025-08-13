from enum import StrEnum
from typing import Optional

import uvicorn
from fastapi import FastAPI, Path, Query

app = FastAPI(redoc_url=None)


class EducationLevel(StrEnum):
    SECONDARY = "Среднее образование"
    SPECIAL = "Среднее специальное образование"
    HIGHER = "Высшее образование"


@app.get(
    "/me",
    tags=["For Me"],
    summary="Приветствие автора",
    description="Тут можно добавить описание",
)
def hello_author():
    return {"Hello": "author"}


@app.get(
    "/{name}",
    tags=["For Users"],
    summary="Приветствие пользователей",
    response_description="Полная строка приветствия",
)
def read_root(
    *,
    name: str = Path(
        min_length=2,
        max_length=20,
        title="Полное имя",
        description="Можно вводить в любом регистре",
    ),
    surname: list[str] = Query(min_length=2, max_length=50),
    age: Optional[int] = Query(None, gt=4, le=99),
    is_staff: bool = Query(False, alias="is-staff", include_in_schema=False),
    education_level: Optional[EducationLevel] = None,
) -> dict[str, str]:
    """
    Либо тут может быть твое описание
    """
    surnames = " ".join(surname)
    result = " ".join([name, surnames])
    result = result.title()
    if age is not None:
        result += ", " + str(age)
    if education_level is not None:
        result += ", " + education_level.lower()
    if is_staff:
        result += ", сотрудник"
    return {"Hello": result}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
