from datetime import date, timedelta

import factory
from factory.fuzzy import FuzzyChoice
from factory.django import DjangoModelFactory

from .models import (
    Address,
    Community,
)


class AddressFactory(DjangoModelFactory):
    class Meta:
        model = Address

    address_1 = factory.Faker("street_address")
    address_2 = factory.Faker("street_address")
    city = factory.Faker("city")
    state = factory.Faker("state")
    zip_code = factory.Faker("pyint", min_value=10000, max_value=99999)


class CommunityFactory(DjangoModelFactory):
    class Meta:
        model = Community

    name = factory.Faker("company")
    description = factory.Faker("paragraph")
    capacity = factory.Faker("pyint", min_value=1, max_value=699)
    phone_number = factory.Faker("phone_number")
    fax_number = factory.Faker("phone_number")

    address = factory.SubFactory(AddressFactory)
