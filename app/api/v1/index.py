from fastapi.routing import APIRouter

router_index = APIRouter()


@router_index.get("/")
async def index():
    return "EV Charger Api"
