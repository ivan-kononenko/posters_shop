from django.db import models
from django.utils.text import slugify
from unidecode import unidecode


class CategoryL1(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(max_length=1000)
    slug = models.SlugField(max_length=50, unique=True)


    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.name))
        super(CategoryL1, self).save(*args, **kwargs)


class CategoryL2(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)
    parent = models.ForeignKey(CategoryL1, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50, unique=True)
    unique_together = ('name', 'parent')

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.name))
        super(CategoryL2, self).save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    category = models.ForeignKey(CategoryL2, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="shop", blank=True)
    slug = models.SlugField(max_length=50, unique=True)
    unique_together = ('name', 'category', 'category_l1.name')

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.name))
        super(Product, self).save(*args, **kwargs)
