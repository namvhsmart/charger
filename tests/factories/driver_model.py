import datetime

import factory.fuzzy
from dateutil.tz import UTC

from app.models.driver import DriverModel
from tests.base_test import SessionTest


class DriverModelFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = DriverModel
        sqlalchemy_session = SessionTest()
        sqlalchemy_session_persistence = "commit"

    id = factory.fuzzy.FuzzyInteger(0, 3)
    name = factory.Faker("name")
    surname = factory.fuzzy.FuzzyText("surname")
    address = factory.fuzzy.FuzzyText("address")
    gender = factory.fuzzy.FuzzyText("gender")
    birth_day = factory.fuzzy.FuzzyDateTime(
        datetime.datetime(1997, 9, 17, tzinfo=UTC),
    )
    card_number = factory.fuzzy.FuzzyInteger(0, 12)
