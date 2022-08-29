from fastapi.routing import APIRouter

from app.schemas.response import resp

charger_model_router = APIRouter()


# @charger_model_router.get("/")
# async def get_all_charger(page_size: int, current_page: int):
#     response = []
#     if current_page >= page_size:
#         return resp.success(data=[])
#     offset = current_page * page_size
#     for i in range(offset - page_size, offset):
#         response.append(db_test[i])
#
#     return resp.success(data=response)


# @charger_model_router.post("/")
# async def create_charger(body: dict):
#     append_data(body)
#     return db_test
#
#
# @charger_model_router.get("/id")
# async def get_charger_by_id(id: int):
#     if db_test[id]:
#         return resp.success(data=db_test[id])
#
#     return resp.success(data=[])
