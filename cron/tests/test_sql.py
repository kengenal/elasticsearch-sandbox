import pytest

from cron.connect import SqlConnect
from cron.sql import UpdateTable

data = [
    {
        'title': 'wix-protos-answers-streams-staging-view-staging-view',
        'author': 'devex-intra@wix.com',
        'link': 'https://pypi.org/project/wix-protos-answers-streams-staging-view-staging-view/',
        'description': 'wix-protos-answers-streams-staging-view-staging-view', 'authors': 'devex-intra@wix.com',
        'version': "0.1"
    }
]


@pytest.fixture(scope="module")
def db():
    path = ":memory:"
    conn = SqlConnect(path=path)
    conn.connect()
    conn.cursor.execute(
        "CREATE TABLE search_pypipackage (id INTEGER PRIMARY KEY,title Char, author CHAR, description TEXT, "
        "link CHAR, "
        "version CHAR, authors CHAR)")
    return conn


@pytest.mark.parametrize("data_fixture", [
    data,
    []
])
def test_create_clear(db, data_fixture):
    try:
        update = UpdateTable(db, data_fixture)
        update.clear_table()
    except Exception as err:
        raise AssertionError(err)


@pytest.mark.parametrize("data_fixture", [
    data,
    []
])
def test_create_create(db, data_fixture):
    try:
        update = UpdateTable(db, data_fixture)
        update.create()
    except Exception as err:
        raise AssertionError(err)
