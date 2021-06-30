# Generated by Django 3.2.4 on 2021-06-30 17:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("address_1", models.CharField(max_length=512)),
                ("address_2", models.CharField(max_length=512)),
                ("city", models.CharField(max_length=128)),
                ("state", models.CharField(max_length=32)),
                ("zip_code", models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name="Community",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                (
                    "description",
                    models.CharField(blank=True, max_length=512, null=True),
                ),
                (
                    "capacity",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(0)]
                    ),
                ),
                ("phone_number", models.CharField(default="", max_length=16)),
                ("fax_number", models.CharField(default="", max_length=16)),
                (
                    "address",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="communities.address",
                    ),
                ),
            ],
        ),
    ]