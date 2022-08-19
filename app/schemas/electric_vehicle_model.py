from app.schemas.base import BaseModelSchemas


class VehicleModelBase(BaseModelSchemas):
    id: str = None
    name: str = None


class VehicleModelResponse(VehicleModelBase):
    """This the serializer exposed on the API"""

    pass


class VehicleModelCreate(VehicleModelBase):
    """This is the serializer used for POST/PATCH requests"""

    pass
