from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

from app.common.database import get_db
from app.crud.driver_crud import driver_model_crud
from app.schemas.driver import DriverModelCreate as DriverCreate
from app.schemas.driver import DriverModelGet, DriverModelUpdate
from app.schemas.response import resp

driver_model_router = APIRouter()


@driver_model_router.get("/")
async def get_list_model(
    params: DriverModelGet = Depends(),
    db: Session = Depends(get_db),
):
    param_dict = params.__dict__

    result = await driver_model_crud.get_list_by_filter(
        db=db,
        filter=param_dict,
        page_size=params.page_size,
        current_page=params.current_page,
        order_by_field=params.order_by_field,
        order_by=params.order_by,
    )
    return resp.success(data=result)


@driver_model_router.get("/")
async def get_list_drivers(db: Session = Depends(get_db)):
    results = await driver_model_crud.list(db)
    return resp.success(data=results)


@driver_model_router.post("/")
async def create_driver(
    request: DriverCreate,
    db: Session = Depends(get_db),
):
    await driver_model_crud.create(db=db, obj_in=request)

    return resp.success(data="Created")


@driver_model_router.get("/{id}")
async def get_driver_by_id(
    id: int,
    db: Session = Depends(get_db),
):
    model = await driver_model_crud.get(db, id)
    return resp.success(data=model)


@driver_model_router.patch("/")
async def patch_driver_details(
    request: DriverModelUpdate,
    db: Session = Depends(get_db),
):
    result = await driver_model_crud.get(db, request.id)
    update = await driver_model_crud.update(
        db=db,
        obj_in=request,
        db_obj=result,
    )
    return resp.success(data=update)


@driver_model_router.get("/records/page")
async def get_list_records(
    current_page: int, page_size: int, db: Session = Depends(get_db)
):
    results = await driver_model_crud.get_multi(
        db=db, skip=(current_page - 1) * page_size, limit=page_size
    )
    return resp.success(data=results)
