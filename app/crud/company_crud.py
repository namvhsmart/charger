from sqlalchemy import asc, desc
from sqlalchemy.orm import Session

from app.crud.base_crud import CRUDBase
from app.models.company_model import CompanyModel
from app.schemas.company_model import (
    CompanyModelCreate,
    CompanyModelFilter,
    CompanyModelUpdate,
)


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
        filter: dict,
        current_page: int,
        page_size: int,
        order_by_field: str,
        order_by: str,
    ) -> list[CompanyModel]:

        data_filter = db.query(CompanyModel)
        body_filter = CompanyModelFilter(**filter).dict()

        for key in body_filter:
            if body_filter[key] is not None:
                data_filter = data_filter.filter(
                    getattr(CompanyModel, key) == filter[key],
                )

        if order_by == "asc":
            data_filter = data_filter.order_by(
                asc(getattr(CompanyModel, order_by_field))
            )
        if order_by == "desc":
            data_filter = data_filter.order_by(
                desc(getattr(CompanyModel, order_by_field))
            )
        offset = (current_page - 1) * page_size
        return data_filter.offset(offset).limit(page_size).all()


company_model_crud = CompanyModelCrud(CompanyModel)
