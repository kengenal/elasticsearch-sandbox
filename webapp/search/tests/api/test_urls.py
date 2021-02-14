import pytest
from django.urls import reverse, resolve

pytestmark = pytest.mark.django_db


def test_search_url_for_api():
    assert (
        reverse("api-search")
        == "/api/search"
    )
    assert resolve("/api/search").view_name == "api-search"
