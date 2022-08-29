from datetime import datetime

from pydantic import BaseModel, Field, conint, constr, validator

from app.common.util import validate_unique
from app.models.driver import DriverModel
from app.schemas.base import BaseModelSchemas


class DriverModelGet(BaseModel):
    page_size: conint(ge=1) | None = None
    current_page: conint(ge=1) | None = None
    name: constr(min_length=2, max_length=255) = None
    card_number: conint(ge=1) | None = None
    order_by: constr(min_length=2, max_length=255) | None = None
    order_by_field: constr(min_length=2, max_length=255) | None = None


class DriverModelFilter(BaseModel):
    name: str = None
    card_number: int = None


class DriverModelBase(BaseModelSchemas):
    id: int = Field(description="The ID that driver")
    name: str = Field(description="Driver's name")
    surname: str = Field(description="Driver's last name")
    address: str = Field(description="Address")
    gender: str = Field(description="Gender")
    birth_day: datetime = Field(description="Birthday")
    card_number: int = Field(description="Card number")


class DriverModelCreate(DriverModelBase):
    @validator("name")
    def unique_check_model(cls, name_check):
        return validate_unique(DriverModel, "name", name=name_check)


class DriverModelUpdate(DriverModelBase):
    pass


class DriverModelResponse(DriverModelBase):
    pass
