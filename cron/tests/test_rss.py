from unittest.mock import Mock

import pytest

from cron.cron.rss import PackagesInfo, merge_authors


class RssDataMock:
    @staticmethod
    def parse():
        return {
            "entries": [

                {
                    "title": "wix-protos-answers-streams-staging-view-staging-view added to PyPI",
                    "title_detail": {
                        "type": "text/plain",
                        "language": None,
                        "base": "https://pypi.org/rss/packages.xml",
                        "value": "wix-protos-answers-streams-staging-view-staging-view added to PyPI"
                    },
                    "links": [
                        {
                            "rel": "alternate",
                            "type": "text/html",
                            "href": "https://pypi.org/project/wix-protos-answers-streams-staging-view-staging-view/"
                        }
                    ],
                    "link": "https://pypi.org/project/wix-protos-answers-streams-staging-view-staging-view/",
                    "id": "https://pypi.org/project/wix-protos-answers-streams-staging-view-staging-view/",
                    "summary": "wix-protos-answers-streams-staging-view-staging-view",
                    "summary_detail": {
                        "type": "text/html",
                        "language": None,
                        "base": "https://pypi.org/rss/packages.xml",
                        "value": "wix-protos-answers-streams-staging-view-staging-view"
                    },
                    "authors": [
                        {
                            "email": "devex-intra@wix.com"
                        }
                    ],
                    "author": "devex-intra@wix.com",
                    "author_detail": {
                        "email": "devex-intra@wix.com"
                    },

                }
            ]}


class RssMockVersion:
    @staticmethod
    def parse():
        return {
            "entries": [
                {"title": "1.0"}
            ]
        }


@pytest.fixture()
def package_info():
    return PackagesInfo(url="URL", version_url="VERSION_URL")


def test_get_package_info_with_correct_url_should_be_return_dictionary(package_info):

    package_info._get_data = Mock(return_value=RssDataMock.parse())
    package_info.get_version = Mock(return_value=RssMockVersion.parse())

    package_info.fetch()

    assert len(package_info.data[0].keys()) == 6


def test_get_package_info_data_parameter_should_be_empty(package_info):
    package_info._get_data = Mock(return_value={"entries": []})
    package_info.get_version = Mock(return_value="")

    assert package_info.data == []


@pytest.mark.parametrize("gets, expect", [
    [[{"email": "test"}, {"email": "test"}], "test:test"],
    [[{"email": "test"}], "test"],
    [[], ""]
])
def test_merge_authors_with_correct_author_list(gets, expect):
    authors = merge_authors(gets)

    assert expect == authors
