from unittest import mock

import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db


def mock_elastic_exception(*args, **kwargs):
    raise Exception()


ELASTIC_PATH = 'search.documents.PypiPackageDocument.get_elastic_data'


class TestPypiView:

    @pytest.mark.parametrize('expect, get_query', [
        [200, {}],
        [404, {'page': 8888}],
        [200, {'filter': 'example'}],
    ])
    def test_with_elastic(self, client, package_model, expect, get_query):
        with mock.patch(ELASTIC_PATH, new=package_model):
            rq = client.get(reverse('search'), get_query)

            assert rq.status_code == expect

    @pytest.mark.parametrize('expect, get_query', [
        [200, {}],
        [404, {'page': 8888}],
        [200, {'filter': 'example'}],
    ])
    def test_with_database(self, client, package_model, expect, get_query):
        with mock.patch(ELASTIC_PATH, new=mock_elastic_exception):
            rq = client.get(reverse('search'), get_query)

            assert rq.status_code == expect
