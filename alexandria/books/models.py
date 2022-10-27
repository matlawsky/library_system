from django.db import models

class Book(models.Model):
    bookId = models.PositiveIntegerField()
    title = models.CharField(max_length=60)
    author = models.CharField(max_length=60)

class CopyBook(Book):
    copyId = models.IntegerField()
    _bookId = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='book',
        )
    availableAt = models.DateField()

# class Comment():
#     commentId = models.PositiveIntegerField()
#     userId = models.ForeignKey()
#     bookId = models.ForeignKey()
#     content = models.TextField()

# class Rating():
#     pass