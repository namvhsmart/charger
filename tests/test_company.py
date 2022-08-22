import logging

from app.config import settings
from tests.base_test import BaseTestCase
from tests.factories.company_model import CompanyModelFactory



class TestCompany(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        CompanyModelFactory.create()

    def test_get_list_company(self):
        response = self.client.get(f"{settings.API_PREFIX}/company")
        res = response.json()
        data = res["data"]
        assert response.status_code == 200
        assert len(data) == 1
    def test_get_company_by_id(self):
        pass
    def test_create_company(self):
        response_create = self.client.post(
                    f"{settings.API_PREFIX}/company/",
                    json = {
                            "name": "Daocm8678 Company",
                            "unit_cost": 8
                    })
        assert response_create.status_code == 200
        response_get = self.client.get(f"{settings.API_PREFIX}/company")
        res = response_get.json()
        data = res['data']
        assert len(data) == 2
    def test_patch_company(self):
        response_patch = self.client.patch(
                    f"{settings.API_PREFIX}/company/",
                    json = {
                        "id": 1,
                        "name": "Daocm",
                        "unit_cost": 6
                    })
        assert response_patch.status_code == 200

        response_get = self.client.get(f"{settings.API_PREFIX}/company")
        res = response_get.json()
        data = res['data']
        assert len(data) == 1
        assert data[0]['name'] == "Daocm"
        assert data[0]['unit_cost'] == 6


