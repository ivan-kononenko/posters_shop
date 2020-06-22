from django.db import models


class CategoryL1(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

class CategoryL2(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)
    parent = models.ForeignKey(CategoryL1, on_delete=models.CASCADE)


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    category = models.ForeignKey(CategoryL2, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
