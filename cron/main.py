from cron.data_synchronize import DataSync
from cron.rss import PackagesInfo

URL = "https://pypi.org/rss/packages.xml"
VERSION_URL = "https://pypi.org/rss/project/{}/releases.xml"


def main():
    try:
        p = PackagesInfo(url=URL, version_url=VERSION_URL)
        p.fetch()
        DataSync(data=p.data).sync_all()
    except Exception as err:
        raise Exception(err)


if __name__ == "__main__":
    main()
