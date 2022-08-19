from sqlalchemy.orm import Session
from app.crud.base_crud import CRUDBase
from app.models.company_model import CompanyModel
from app.schemas.company_model import CompanyModelCreate, CompanyModelUpdate


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


company_model_crud = CompanyModelCrud(CompanyModel)
