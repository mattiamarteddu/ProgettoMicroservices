from django.db import models

# Create your models here.
# Create your models here.
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    birthday_date = models.DateTimeField('date published')

    def __str__(self):
        return str(self.name) + str(self.surname)
