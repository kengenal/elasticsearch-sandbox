from django.db import models

from django.db.models import Q


class PypiPackage(models.Model):
    title = models.CharField(max_length=120)
    author = models.EmailField(max_length=120)
    description = models.TextField(max_length=255)
    link = models.URLField()
    version = models.CharField(max_length=10)
    authors = models.CharField(max_length=255)

    @staticmethod
    def get_db_data(fil):
        if fil:
            return PypiPackage.objects.filter(
                Q(author__icontains=fil)
                | Q(version__icontains=fil)
                | Q(authors__icontains=fil)
                | Q(author__icontains=fil)
                | Q(title__icontains=fil)
            ).all()
        return PypiPackage.objects.all()

