from app.schemas.base import BaseModelSchemas
from app.common.util import validate_unique
from pydantic import Field, constr, validator
from app.models.company_model import CompanyModel

class CompanyModelBase(BaseModelSchemas):
    id: int = None
    name: str = None
    unit_cost: float = None


class CompanyModelCreate(CompanyModelBase):
    pass

class CompanyModelUpdate(CompanyModelBase):
    created_at: str = None

class CompanyModelResponse(CompanyModelBase):
    pass