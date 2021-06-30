import uuid

from django.db import models
from django.core.validators import MinValueValidator


class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    address_1 = models.CharField(max_length=512)
    address_2 = models.CharField(max_length=512)
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=32)
    zip_code = models.CharField(max_length=32)

    @property
    def city_state_zip(self):
        """Helper for Forms that split second part of address"""
        return f"{self.city}, {self.state}, {self.zip_code}"

    def __str__(self):
        return f"{self.address_1}, {self.address_2}, {self.city}, {self.state}, {self.zip_code}"


class Community(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=512, null=True, blank=True)

    # If address is deleted, set address_id to null in db
    address = models.ForeignKey(
        Address, null=True, blank=True, on_delete=models.SET_NULL
    )

    capacity = models.IntegerField(
        # We'll get this validation for free with Model Serializer
        validators=[MinValueValidator(0)]
    )
    phone_number = models.CharField(max_length=16, default="")
    fax_number = models.CharField(max_length=16, default="")

    def __str__(self):
        return f"<Community (name={self.name}) >"
