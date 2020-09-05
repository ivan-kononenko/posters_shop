from django.db import models
from django.utils.crypto import get_random_string
from django.utils.text import slugify
import os
from PIL import Image
from unidecode import unidecode

from django.conf import settings

SIZES = {
            "thumb": 100,
            "small": 300,
            "big": 800
        }


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

    class Meta:
        unique_together = ('slug', 'parent')

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
    image_small = models.ImageField(upload_to="shop", blank=True)
    image_thumb = models.ImageField(upload_to="shop", blank=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        unique_together = ('slug', 'category')

    def __init__(self, *args, **kwargs):
        super(Product, self).__init__(*args, **kwargs)
        self._image_old = self.image

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.name))

        if self.image != self._image_old:
            image_name_new = get_random_string(8)

            image_name = os.path.join("shop", f"{image_name_new}.jpeg")
            image_path = os.path.join(settings.MEDIA_ROOT, image_name)
            img = Image.open(self.image)
            img = img.resize((SIZES["big"], SIZES["big"]), Image.ANTIALIAS)
            img.save(image_path, format="JPEG", quality=70, optimize=True)
            self.image.name = image_name

            image_name = os.path.join("shop", f"{image_name_new}_small.jpeg")
            image_path = os.path.join(settings.MEDIA_ROOT, image_name)
            img = Image.open(self.image)
            img = img.resize((SIZES["small"], SIZES["small"]), Image.ANTIALIAS)
            img.save(image_path, format="JPEG", quality=70, optimize=True)
            self.image_small.name = image_name

            image_name = os.path.join("shop", f"{image_name_new}_thumb.jpeg")
            image_path = os.path.join(settings.MEDIA_ROOT, image_name)
            img = Image.open(self.image)
            img = img.resize((SIZES["thumb"], SIZES["thumb"]), Image.ANTIALIAS)
            img.save(image_path, format="JPEG", quality=70, optimize=True)
            self.image_thumb.name = image_name

        super(Product, self).save(*args, **kwargs)
