from django.db import models
from django.contrib.auth.models import AbstractUser


class Patient(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True, null=False, blank=False)

    def __str__(self):
        return self.username
