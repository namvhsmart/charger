from dateutil.parser import parser
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
             params: dict,
             current_page: int,
             page_size: int,
             order_by_field: str,
             order_by: str) -> list[CompanyModel]:
        data_filter = db.query(CompanyModel)



        if "name" in params:
            data_filter = data_filter.filter(CompanyModel.name == params["name"])
        if "unit_cost" in params:
            data_filter = data_filter.filter(CompanyModel.unit_cost == params["unit_cost"])

        if order_by_field == "name" and order_by == "asc":
            data_filter = data_filter.order_by(CompanyModel.name.asc())

        if order_by_field == "name" and order_by == "desc":
            data_filter = data_filter.order_by(CompanyModel.name.desc())

        if order_by_field == "unit_cost" and order_by == "asc":
            data_filter = data_filter.order_by(CompanyModel.unit_cost.asc())

        if order_by_field == "unit_cost" and order_by == "desc":
            data_filter = data_filter.order_by(CompanyModel.unit_cost.asc())


        # return db.query(CompanyModel).all()
        return data_filter.offset((current_page-1)*page_size).limit(page_size).all()


company_model_crud = CompanyModelCrud(CompanyModel)
