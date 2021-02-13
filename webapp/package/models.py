from django.db import models


# Create your models here.

class PypiPackage(models.Model):
    title = models.TextField(max_length=255)
    author = models.EmailField(max_length=120)
    link = models.URLField()
    description = models.TextField(max_length=255)
    authors = models.TextField(max_length=200)

    class Meta:
        db_table = "pypi_package"
