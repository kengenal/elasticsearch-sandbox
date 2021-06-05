import pytest
from django.core.management import call_command

from search.management.commands import rss_fetch
from search.models import PypiPackage


def mock(*args, **kwargs):
    return None


@pytest.mark.django_db
class TestRssFetch:
    def test_fetch_with_correct_data_results_should_be_in_database(self, monkeypatch, package_model):
        monkeypatch.setattr(rss_fetch, "build_index", mock)
        call_command("rss_fetch")

        obj = PypiPackage.objects.all()
        assert obj.count() > 0
