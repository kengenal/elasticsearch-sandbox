
from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from .models import PypiPackage


@registry.register_document
class PypiPackageDocument(Document):
    class Index:
        name = 'pypi_package'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = PypiPackage

        fields = [
            'title',
            'author',
            'description',
            'link',
            'version',
            'authors'
        ]
