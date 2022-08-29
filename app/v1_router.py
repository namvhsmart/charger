from fastapi import APIRouter

from app.api.v1.auth_router import auth_router
from app.api.v1.charger_model_router import charger_model_router
from app.api.v1.company_router import company_model_router
from app.api.v1.current_user_router import current_user_router
from app.api.v1.index import router_index
from app.api.v1.user_router import user_router
from app.api.v1.vehicle_model_router import vehicle_model
from app.api.v1.charger_router import charger_router

api_v1_router = APIRouter()

# router index
api_v1_router.include_router(router_index)

# router charger model
api_v1_router.include_router(
    charger_model_router, prefix="/charger-model"
)

api_v1_router.include_router(
    charger_router, prefix="/charger"
)

# router vehicle model
api_v1_router.include_router(
    vehicle_model, prefix="/vehicle-model"
)
api_v1_router.include_router(
    auth_router,
    prefix="/authentication",
)

api_v1_router.include_router(
    current_user_router,
    prefix="/current_user",
)
api_v1_router.include_router(
    user_router,
    prefix="/user",
)
api_v1_router.include_router(
    company_model_router,
    prefix="/company",
)
