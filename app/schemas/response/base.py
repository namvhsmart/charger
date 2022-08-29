from pydantic import BaseModel


class PaginationModel(BaseModel):
    total: int
    page: int
    page_size: int
    data: list
