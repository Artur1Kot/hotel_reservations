from fastapi import Depends, Query
from pydantic import BaseModel
from typing import Annotated



class PaginationParams(BaseModel):
    page: Annotated[int | None, Query(default=1, ge=1)]
    per_page: Annotated[int | None, Query(default=4, ge=1, lt=10)]


PaginationDep = Annotated[PaginationParams, Depends()]