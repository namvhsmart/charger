from pydantic import BaseModel


class BaseModelSchemas(BaseModel):
    created_at: str = None
    updated_at: str = None
    updated_by: str = None
    created_by: str = None
