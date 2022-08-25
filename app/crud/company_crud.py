from sqlalchemy import and_
from sqlalchemy.orm import Session
from app.crud.base_crud import CRUDBase
from app.models.company_model import CompanyModel
from app.schemas.company_model import CompanyModelCreate, CompanyModelUpdate, CompanyModelBase


class CompanyModelCrud(
    CRUDBase[
        CompanyModel,
        CompanyModelCreate,
        CompanyModelUpdate,
    ]
):
    async def list_by_name(
            self,
            db: Session,
            name: str,
            ) -> list[CompanyModel]:
        return db.query(CompanyModel).filter(CompanyModel.name == name).all()

    async def get_list_by_filter(
            self,
             db: Session,
             params: object,) -> list[CompanyModel]:
        data_filter = db.query(CompanyModel)

        if "name" in params:
            data_filter = data_filter.filter(CompanyModel.name == params['name'])
        if "unit_cost" in params:
            data_filter = data_filter.filter(CompanyModel.unit_cost == params['unit_cost'])

        return data_filter.all()


company_model_crud = CompanyModelCrud(CompanyModel)
