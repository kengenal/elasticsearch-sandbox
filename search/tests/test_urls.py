import pytest
from django.urls import reverse, resolve

pytestmark = pytest.mark.django_db


def test_search_url():
    assert (
        reverse("search")
        == "/"
    )
    assert resolve("/").view_name == "search"
