from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

class Account(models.Model):
    name = models.CharField(max_length=50)
    budget = models.IntegerField()

class Category(models.Model):
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    budget = models.IntegerField()

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    budget = models.IntegerField()

class Method(models.Model):
    name = models.CharField(max_length=50)

class Report(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    payment = models.ForeignKey(Method, on_delete=models.PROTECT)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.PROTECT)
    date = models.DateField(default=timezone.now)
    price = models.CharField(max_length=10)
    description = models.TextField(max_length= 50)
    

# terminar los modelos, extened user, bootstrap, llenar la base de datos, relaciones entre tablas, on delete