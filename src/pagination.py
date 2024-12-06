from fastapi_pagination.bases import AbstractPage,AbstractParams,RawParams
from pydantic import BaseModel
from fastapi import Query
from typing import TypeVar,Generic,Sequence

T = TypeVar("T")

class Params(BaseModel,AbstractParams):
    page: int = Query(1,ge=1,description="Page number")
    size: int = Query(20,gt=0,le=100,description="Page size")
    


class Page(AbstractPage[T],Generic):
    data: Sequence[T]
    total: int
    page: int
    size: int
    next: str
    previous: str
    total_pages: int

