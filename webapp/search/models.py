from django.db import models


# Create your models here.

class PypiPackage(models.Model):
    title = models.CharField(max_length=120)
    author = models.EmailField(max_length=120)
    description = models.TextField(max_length=255)
    link = models.URLField()
    version = models.CharField(max_length=10)
    authors = models.CharField(max_length=255)
