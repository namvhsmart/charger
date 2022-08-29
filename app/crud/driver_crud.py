from sqlalchemy import asc, desc
from sqlalchemy.orm import Session

from app.crud.base_crud import CRUDBase
from app.models.driver import DriverModel
from app.schemas.base import BaseModelSchemas
from app.schemas.driver import DriverModelCreate as DriverCreate
from app.schemas.driver import DriverModelFilter as DriverFilter
from app.schemas.driver import DriverModelUpdate


class DriverModelBase(BaseModelSchemas):
    id: int = None
    name: str = None
    surname: str = None
    address: str = None
    gender: str = None
    birth_day: str = None
    card_number: str = None


class DriverModelCRUD(
    CRUDBase[DriverModel, DriverCreate, DriverModelUpdate],
):
    async def get_list_by_filter(
        self,
        db: Session,
        filter: dict,
        current_page: int,
        page_size: int,
        order_by_field: str,
        order_by: str,
    ) -> list[DriverModel]:
        data_filter = db.query(DriverModel)
        body_filter = DriverFilter(**filter).dict()

        for key in body_filter:
            if body_filter[key] is not None:
                data_filter = data_filter.filter(
                    getattr(DriverModel, key) == filter[key],
                )

        if order_by == "asc":
            data_filter = data_filter.order_by(
                asc(getattr(DriverModel, order_by_field))
            )
        if order_by == "desc":
            data_filter = data_filter.order_by(
                desc(getattr(DriverModel, order_by_field))
            )
        offset = (current_page - 1) * page_size
        data = data_filter.offset(offset).limit(page_size).all()
        total = data_filter.offset(offset).limit(page_size).count()

        return {"data": data, "total": total}


driver_model_crud = DriverModelCRUD(DriverModel)
