from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=60, unique=True)
    country = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=60, unique=True)

    class Meta:
        verbose_name = "Driver"


    def __str__(self):
            return f"{self.username} ({self.license_number})"


class Car(models.Model):
    model = models.CharField(max_length=60)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars"
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="cars"
    )

    def __str__(self):
        return self.model