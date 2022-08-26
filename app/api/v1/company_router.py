import json

from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

from app.common.database import get_db
from app.crud.company_crud import company_model_crud
from app.schemas.company_model import (
    CompanyModelCreate,
    CompanyModelGet,
    CompanyModelUpdate,
)
from app.schemas.response import resp

company_model_router = APIRouter()


async def check_params(filter: str | None = None):
    if filter:
        return json.loads(filter)
    return {}


@company_model_router.get("/test")
async def get_list_model(filter: CompanyModelGet = Depends()):
    return filter


@company_model_router.get("/")
async def get_list_by_filter(
    filter: dict = Depends(check_params), db: Session = Depends(get_db)
):
    page_size = filter.pop("page_size", 10)
    current_page = filter.pop("current_page", 1)
    order_by_field = filter.pop("order_by_field", "name")
    order_by = filter.pop("order_by", "desc")

    result = await company_model_crud.get_list_by_filter(
        db=db,
        params=filter,
        page_size=page_size,
        current_page=current_page,
        order_by_field=order_by_field,
        order_by=order_by,
    )
    return resp.success(data=result)


@company_model_router.get("/{id}")
async def get_company_by_id(
    id: int,
    db: Session = Depends(get_db),
):
    model = await company_model_crud.get(db, id)
    return resp.success(data=model)


@company_model_router.post("/")
async def create_comapny(
    body_data: CompanyModelCreate, db: Session = Depends(get_db)
) -> str:
    await company_model_crud.create(db=db, obj_in=body_data)
    return resp.success(data="Created")


@company_model_router.patch("/")
async def patch_company_details(
    request: CompanyModelUpdate, db: Session = Depends(get_db)
):
    result = await company_model_crud.get(db, request.id)
    update = await company_model_crud.update(
        db=db,
        obj_in=request,
        db_obj=result,
    )
    return resp.success(data=update)
