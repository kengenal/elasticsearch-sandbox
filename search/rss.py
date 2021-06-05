import feedparser


def merge_authors(authors):
    auth = []
    if authors:
        auth = [x["email"] for x in authors]
    return ":".join(auth)


class PackagesInfo:
    def __init__(self, url, version_url):
        """
        Get package info from pypi
        :param url:
        :param version_url:
        """
        self.url = url
        self.data = []
        self.data_without_simplify = {}
        self.version_url = version_url

    def fetch(self):
        """ fetch data and put to global data variable """
        d = self._get_data()
        self.data_without_simplify = d.get("entries")
        self.data = d.get("entries")
        self._data_simplify()

    def _get_data(self):
        return feedparser.parse(self.url)

    def _data_simplify(self):
        new_data = []
        for entries in self.data:
            title = entries.get("title").replace("added to PyPI", "").strip()
            new_data.append({
                "title": title,
                "author": entries.get("author"),
                "link": entries.get("link"),
                "description": entries.get("summary"),
                "authors": merge_authors(entries.get("authors")),
                "version": self.get_version(title)
            })
        self.data = new_data

    def get_version(self, name):
        try:
            d = feedparser.parse(self.version_url.format(name))
            return d["entries"][0]["title"]
        except KeyError:
            return None
