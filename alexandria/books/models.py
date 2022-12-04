from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=60)
    author = models.CharField(max_length=60)
    pages = models.PositiveSmallIntegerField()
    description = models.TextField()
    ISBN = models.IntegerField()
    release_date = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})

    def summary(self):
        return self.description[:100]


class CopyBook(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
    )
    availableAt = models.DateField(auto_now_add=True)
