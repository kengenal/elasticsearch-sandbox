import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db


def test_index(client, package_model):
    rq = client.get(reverse('search'))

    assert rq.status_code == 200