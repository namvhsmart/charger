from pydantic import validator

from app.common.util import validate_unique
from app.models.company_model import CompanyModel
from app.schemas.base import BaseModelSchemas


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


class CompanyModelResponse(CompanyModelBase):
    pass
