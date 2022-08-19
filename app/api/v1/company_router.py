from typing import List

from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from app.common.handle_error import BadRequestException, NotFoundException

from app.common.database import get_db
from app.common.logger import logger
from app.crud.company_crud import company_model_crud
from app.schemas.company_model import CompanyModelCreate, CompanyModelResponse
from app.schemas.response import resp

company_model_router = APIRouter()

@company_model_router.get("/")
async def get_list_companys(db: Session = Depends(get_db)):
    results = await company_model_crud.list(db)
    return resp.success(data=results)

@company_model_router.post("/")
async def create_comapny(request: CompanyModelCreate ,db: Session = Depends(get_db)) -> str:
    model = await company_model_crud.get(db, request.__dict__["name"])

    if model:
        raise BadRequestException(message="Name already exists")

    await company_model_crud.create(db = db, obj_in= request)

    return resp.success(data="Created")

