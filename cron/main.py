from cron.connect import ElasticConnect
from cron.elastic import Index
from cron.rss import PackagesInfo

URL = "https://pypi.org/rss/packages.xml"
VERSION_URL = "https://pypi.org/rss/project/{}/releases.xml"


def main():
    try:
        p = PackagesInfo(url=URL, version_url=VERSION_URL)
        p.fetch()
        print(p.data)
        conn = ElasticConnect()
        conn.connect()
        i = Index(es=conn.es, data=p.data)
        i.clear_index()
        i.create()
    except Exception as err:
        raise Exception(err)


if __name__ == "__main__":
    main()