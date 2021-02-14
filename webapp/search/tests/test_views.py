import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db


class TestPypiView:
    def test_without_any_parameters_should_be_return_status_ok(self, client, package_model):
        rq = client.get(reverse('search'))

        assert rq.status_code == 200

    def test_without_with_filter_parameters_should_be_return_status_ok(self, client, package_model):
        rq = client.get(reverse('search'), {'filter': 'example'})

        assert rq.status_code == 200

    def test_without_with_pagination_should_be_return_status_not_found(self, client, package_model):
        rq = client.get(reverse('search'), {'page': '8888'})

        assert rq.status_code == 404
