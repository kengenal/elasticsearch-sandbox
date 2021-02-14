from unittest import mock

import pytest
from django.urls import reverse

from search.tests.test_views import ELASTIC_PATH, mock_elastic_exception

pytestmark = pytest.mark.django_db


class TestApiPypiView:
    @pytest.mark.parametrize('expect, get_query', [
        [200, {}],
        [404, {'page': 8888}],
        [200, {'filter': 'example'}],
    ])
    def test_with_elastic(self, client, package_model, expect, get_query):
        with mock.patch(ELASTIC_PATH, new=package_model):
            rq = client.get(reverse('api-search'), get_query)

            assert rq.status_code == expect

    @pytest.mark.parametrize('expect, get_query', [
        [200, {}],
        [404, {'page': 8888}],
        [200, {'filter': 'example'}],
    ])
    def test_with_database(self, client, package_model, expect, get_query):
        with mock.patch(ELASTIC_PATH, new=mock_elastic_exception):
            rq = client.get(reverse('api-search'), get_query)

            assert rq.status_code == expect
