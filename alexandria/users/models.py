from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date


class CustomUser(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    user_registration_date = models.DateField(default=date.today)
