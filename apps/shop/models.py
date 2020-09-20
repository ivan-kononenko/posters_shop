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

    def _get_new_sizes(self, old_size, image_type="thumb"):
        width, height = old_size
        if height > width:
            k = height / SIZES[image_type]
            new_height = SIZES[image_type]
            new_width = width / k
        else:
            k = width / SIZES[image_type]
            new_width = SIZES[image_type]
            new_height = height / k
        return int(new_width), int(new_height)

    def _resize_save_image(self, image_name_new, image_type="thumb"):
        image_name_new = os.path.join(f"{image_name_new}_{image_type}.jpeg")
        image_path = os.path.join(settings.MEDIA_ROOT, "shop", image_name_new)
        img = Image.open(self.image)
        img = img.convert('RGB')
        new_size = self._get_new_sizes(
            (self.image.width, self.image.height,), image_type)
        img = img.resize(new_size, Image.ANTIALIAS)
        img.save(image_path, format="JPEG", quality=70, optimize=True)

    def _delete_old_images(self):
        image_name, image_type = os.path.basename(self._image_old.name).split(".")
        image_path = os.path.join(settings.MEDIA_ROOT, "shop", f"{image_name}_big.{image_type}")
        os.unlink(image_path)
        image_path = os.path.join(settings.MEDIA_ROOT, "shop", f"{image_name}_small.{image_type}")
        os.unlink(image_path)
        image_path = os.path.join(settings.MEDIA_ROOT, "shop", f"{image_name}_thumb.{image_type}")
        os.unlink(image_path)
        self._image_old.delete()

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.name))
        if self.image and self.image != self._image_old:
            image_name_new = get_random_string(8)
            self._resize_save_image(image_name_new, "big")
            self._resize_save_image(image_name_new, "small")
            self._resize_save_image(image_name_new, "thumb")
            # self.image.name = os.path.join(f"{image_name_new}.jpeg")
            if self._image_old:
                print(self._image_old.name)
                # self._delete_old_images()

        super(Product, self).save(*args, **kwargs)
