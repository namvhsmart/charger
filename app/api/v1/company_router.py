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


@company_model_router.get("/")
async def get_list_model(
    params: CompanyModelGet = Depends(),
    db: Session = Depends(get_db),
):
    param_dict = params.__dict__

    result = await company_model_crud.get_list_by_filter(
        db=db,
        filter=param_dict,
        page_size=params.page_size,
        current_page=params.current_page,
        order_by_field=params.order_by_field,
        order_by=params.order_by,
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
