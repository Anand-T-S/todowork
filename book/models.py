from django.db import models

# Create your models here.
class Books(models.Model):
    book_name=models.CharField(max_length=120)
    author=models.CharField(max_length=120)
    pages=models.PositiveIntegerField()
    price=models.PositiveIntegerField()

    def __str__(self):
        return self.book_name