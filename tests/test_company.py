import logging

from app.config import settings
from tests.base_test import BaseTestCase
from tests.factories.company_model import CompanyModelFactory



class TestCompany(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        CompanyModelFactory.create()

    def test_list(self):
        response = self.client.get(f"{settings.API_PREFIX}/company")
        res = response.json()
        assert res["data"][0]["id"] == 1


