import factory.fuzzy

from app.models.company_model import CompanyModel
from tests.base_test import SessionTest


class CompanyModelFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = CompanyModel
        sqlalchemy_session = SessionTest()
        sqlalchemy_session_persistence = "commit"

    name = factory.Faker("name")
    unit_cost = factory.fuzzy.FuzzyFloat(34)
