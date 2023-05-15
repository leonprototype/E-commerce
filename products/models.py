from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    stock = models.IntegerField()
    description = models.CharField(max_length=250, null=True, blank=True)
    brand = models.ForeignKey(
        Brand, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Carrito(models.Model):
    # $usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
