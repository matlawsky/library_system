from django.db import models

class User(models.Model):
    userId = models.PositiveIntegerField()
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)

class Reader(User):
    availableAt = models.DateField()
    account_balance = models.FloatField()

class Worker(User):
    pass