from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

from app.common.database import DBBaseCustom, engine
from app.common.handle_error import APIException
from app.core.config import get_settings, Settings
from app.v1_router import api_v1_router


def create_app() -> FastAPI:
    """
    Create object FatAPI
    :return:
    """
    settings = get_settings()

    app = FastAPI(
        title=settings.TITLE,
        description=settings.DESCRIPTION,
        version=settings.VERSION,
        docs_url=None,
    )

    register_cors(app, settings)
    register_router(app)
    register_exception(app)

    @app.on_event("startup")
    async def startup_event():
        DBBaseCustom.metadata.create_all(bind=engine)

    return app


def register_router(app: FastAPI) -> None:
    """
    Register route
    :param app:
    :return:
    """
    app.include_router(api_v1_router)


def register_cors(app: FastAPI, settings: Settings) -> None:
    """
    Register cors
    :param app:
    :return:
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def register_exception(app: FastAPI) -> None:
    """
    Register exception
    exception_handler
    exception_handlers
    TypeError: 'dict' object is not callable
    :param app:
    :return:
    """

    @app.exception_handler(APIException)
    async def unicorn_exception_handler(request: Request, exc: APIException):
        return JSONResponse(
            status_code=exc.http_status,
            content={"message": f"{exc.message}"},
        )
