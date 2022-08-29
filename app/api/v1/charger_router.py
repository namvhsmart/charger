from fastapi.routing import APIRouter

from app.mock_data.charger import get_chargers
from app.schemas.response.base import PaginationModel

charger_router = APIRouter()


@charger_router.get("/", response_model=PaginationModel)
async def get_all_charger(page_size: int, page: int):
    chargers = get_chargers()
    paginator = [chargers[i:i + page_size] for i in range(0, len(chargers), page_size)]

    return {
        "total": 20,
        "data": paginator[page],
        "page": page,
        "page_size": page_size
    }
