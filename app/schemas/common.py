from pydantic import BaseModel, Field


class Common(BaseModel):
    name: str = Field(max_length=100)

    class Config:
        str_min_length = 1


class CategoriesCreate(Common): ...  # noqa: E701


class LanguagesCreate(Common): ...  # noqa: E701


class StatusesCreate(Common): ...  # noqa: E701


class CommonDB(Common):
    id: int

    class Config:
        orm_mode = True
