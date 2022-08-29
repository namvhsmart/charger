from pydantic import BaseModel, confloat, conint, constr, validator

from app.common.util import validate_id, validate_unique
from app.models.company_model import CompanyModel
from app.schemas.base import BaseModelSchemas


class CompanyModelGet(BaseModel):
    page_size: conint(ge=1) | None = None
    current_page: conint(ge=1) | None = None
    name: constr(min_length=2, max_length=255) = None
    unit_cost: confloat(ge=0) | None = None
    order_by: constr(min_length=2, max_length=255) | None = None
    order_by_field: constr(min_length=2, max_length=255) | None = None


class CompanyModelFilter(BaseModel):
    name: str = None
    unit_cost: float = None


class CompanyModelBase(BaseModelSchemas):
    id: int = None
    name: str = None
    unit_cost: float = None


class CompanyModelCreate(CompanyModelBase):
    @validator("name")
    def unique_check_model(cls, name_check):
        return validate_unique(CompanyModel, "name", name=name_check)


class CompanyModelUpdate(CompanyModelBase):
    @validator("name")
    def unique_check_model(cls, name_check):
        return validate_unique(CompanyModel, "name", name=name_check)

    @validator("id")
    def unique_check_id(cls, id):
        return validate_id(CompanyModel, "id", id=id)


class CompanyModelResponse(CompanyModelBase):
    pass
