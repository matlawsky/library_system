from django.db import models
from django.urls import reverse
from django.conf import settings
from books.models import Book


class Reaction(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class Vote(Reaction):
    rating = models.FloatField()


class Comment(Reaction):
    body = models.TextField()
