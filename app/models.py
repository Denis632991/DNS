from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    describe = models.CharField(max_length=255)
    price = models.IntegerField()
    number = models.IntegerField()


class Sklad(models.Model):
    name = models.IntegerField()
    products = models.ForeignKey(Product, on_delete=models.CASCADE)

class Dostavka(models.Model):
    city = models.CharField(max_length=255)
    city_off = models.ForeignKey(Sklad, on_delete=models.CASCADE)
    cost_of_dostavka = models.IntegerField()