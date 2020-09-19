from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=1000, blank=True, null=True)

    def __repr__(self):
        return f"{self.last_name} {self.last_name}"

    def __str__(self):
        return f"{self.last_name} {self.last_name}"
