import pytest

from search.tests.factories import PackageInfoFactory


@pytest.fixture()
def package_model():
    return PackageInfoFactory()

