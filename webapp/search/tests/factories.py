from random import randint

import factory
from factory import Faker


class PackageInfoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'search.PypiPackage'
        django_get_or_create = ('title', 'author', 'link', 'version', 'description', 'authors')

    title = Faker('user_name')
    author = Faker('name')
    link = "http://test.com"
    version = factory.Sequence(lambda n: str(randint(0, 10)))
    description = Faker('user_name')
    authors = Faker('name')
