from django.db import models
from django.utils import timezone

class Report(models.Model):
    date = models.DateField(default=timezone.now)
    price = models.CharField(max_length=10)
    description = models.TextField(max_length= 50)

# terminar los modelos, extened user, bootstrap, llenar la base de datos, relaciones entre tablas, on delete
# mvp minimal viable product
# linux



# class Account(models.Model):
#     name = models.CharField(max_length=50)
#     budget = models.IntegerField()

# class Category(models.Model):
#     name = models.CharField(max_length=50)
#     budget = models.IntegerField()