# Create your models here.
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.title) + " || " + str(self.author)
