from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)

    def is_admin(self):
        return self.is_admin

class Region(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Country(models.Model):
    code = models.CharField(max_length=2)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.code
