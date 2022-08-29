from app.config import settings
from tests.base_test import BaseTestCase
from tests.factories.driver_model import DriverModelFactory


class TestDriver(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        DriverModelFactory.create()

    def test_get_list_driver(self):
        response = self.client.get(f"{settings.API_PREFIX}/driver")
        res = response.json()
        data = res["data"]
        assert response.status_code == 200
        assert len(data) == 1

    def test_get_driver_by_id(self):
        pass


class TestCreateDriver(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        DriverModelFactory.create()

    def test_create_driver(self):
        data = {
            "id": 1,
            "name": "Tobi2",
            "surname": "Nguyen",
            "address": "Hai Duong",
            "gender": "Nam",
            "birth_day": "1997-04-04 17:05:32.327",
            "card_number": 1997,
        }
        response = self.client.post(
            f"{settings.API_PREFIX}/driver/",
            json=data,
        )
        assert response.status_code == 200
        response_get = self.client.get(
            f"{settings.API_PREFIX}/driver",
        )
        res = response_get.json()
        data = res["data"]
        assert len(data) == 2


class TestUpdateDriver(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        DriverModelFactory.create()

    def test_patch_driver(self):
        response_patch = self.client.patch(
            f"{settings.API_PREFIX}/driver/",
            json={
                "id": 1,
                "name": "Tobi2",
                "surname": "Nguyen",
                "address": "Hai Duong",
                "gender": "Nam",
                "birth_day": "1997-04-04T17:05:32",
                "card_number": 1997,
            },
        )
        assert response_patch.status_code == 200
        response_get = self.client.get(f"{settings.API_PREFIX}/driver/")
        res = response_get.json()
        data = res["data"]
        assert len(data) == 1
        assert data[0]["name"] == "Tobi2"
        assert data[0]["surname"] == "Nguyen"
        assert data[0]["address"] == "Hai Duong"
        assert data[0]["gender"] == "Nam"
        assert data[0]["birth_day"] == "1997-04-04T17:05:32"
        assert data[0]["card_number"] == 1997
