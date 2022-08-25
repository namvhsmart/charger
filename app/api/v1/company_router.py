from typing import List

from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from app.common.handle_error import BadRequestException, NotFoundException

from app.common.database import get_db
from app.common.logger import logger
from app.crud.company_crud import company_model_crud
from app.models.company_model import CompanyModel
from app.schemas.company_model import CompanyModelCreate, CompanyModelResponse, CompanyModelUpdate
from app.schemas.response import resp

company_model_router = APIRouter()

async def check_params(filter: str | None = None, name: str | None = None, unit_cost:int | None = None):
    response = {}
    print(filter)
    print(name)
    if filter:
        response['filter'] = filter
    if name:
        response['name'] = name
    if unit_cost:
        response['unit_cost'] = unit_cost
    return response

@company_model_router.get("/test")
async def get_list_by_filter(params: dict = Depends(check_params), db: Session = Depends(get_db)):
    print(params)
    result = await company_model_crud.get_list_by_filter(db=db, params=params)
    return resp.success(data=result)

@company_model_router.get("/")
async def get_list_companys( current_page: int,page_size: int ,  db: Session = Depends(get_db)):
    results = await company_model_crud.get_multi(db = db, skip=(current_page-1)*page_size, limit=page_size)
    return resp.success(data=results)

@company_model_router.get("/{id}")
async def get_company_by_id(id: int, db: Session = Depends(get_db), ):
    model = await company_model_crud.get(db,id)
    return resp.success(data=model)

@company_model_router.post("/")
async def create_comapny(body_data: CompanyModelCreate ,db: Session = Depends(get_db)) -> str:

    await company_model_crud.create(db = db, obj_in= body_data)
    return resp.success(data="Created")


@company_model_router.patch("/")
async def patch_company_details(request: CompanyModelUpdate, db: Session = Depends(get_db)):
    print(request.id)
    result = await company_model_crud.get(db, request.id)
    update = await company_model_crud.update(db = db, obj_in= request,db_obj=result)
    return resp.success(data=update)

