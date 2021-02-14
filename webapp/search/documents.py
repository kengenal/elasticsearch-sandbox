from django.conf import settings
from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from elasticsearch_dsl import Q

from .models import PypiPackage


@registry.register_document
class PypiPackageDocument(Document):
    class Index:
        name = 'pypi_package'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = PypiPackage
        queryset_pagination = settings.PAGINATION
        fields = [
            'title',
            'author',
            'description',
            'link',
            'version',
            'authors'
        ]

    @staticmethod
    def get_elastic_data(fil):
        if fil:
            return PypiPackageDocument.search().filter(
                Q("match", title=fil)
                | Q("match", title=fil)
                | Q("match", author=fil)
                | Q("match", authors=fil)
                | Q("match", title=fil)
            )
        return PypiPackageDocument.search()
