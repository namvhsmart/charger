from app.schemas.base import BaseModelSchemas
from app.common.util import validate_unique
from pydantic import Field, constr, validator
from app.models.company_model import CompanyModel

class CompanyModelBase(BaseModelSchemas):
    id: int = None
    name: str = None
    unit_cost: float = None


class CompanyModelCreate(CompanyModelBase):
    @validator("name")
    def unique_check_model(cls, name_check):
        return validate_unique(CompanyModel, "name", name  = name_check)

class CompanyModelUpdate(CompanyModelBase):
    @validator("name")
    def unique_check_model(cls, name_check):
        return validate_unique(CompanyModel, "name", name=name_check)

class CompanyModelResponse(CompanyModelBase):
    pass