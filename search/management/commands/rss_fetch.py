from django.core.management import call_command
from django.core.management.base import BaseCommand

from search.models import PypiPackage
from search.rss import PackagesInfo

URL = "https://pypi.org/rss/packages.xml"
VERSION_URL = "https://pypi.org/rss/project/{}/releases.xml"


def build_index():
    call_command("search_index", "--rebuild")


class Command(BaseCommand):
    help = "fetch data from pypi and push to database"

    def handle(self, *args, **options):
        p = PackagesInfo(url=URL, version_url=VERSION_URL)
        p.fetch()
        data = p.data
        PypiPackage.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Clear table"))

        for i in data:
            p = PypiPackage()
            p.author = i['author'] or "undefined"
            p.description = i["description"]
            p.link = i["link"]
            p.version = i["version"]
            p.authors = i['authors'] or "undefined"
            p.save()
        build_index()
        self.stdout.write(self.style.SUCCESS("All data has been saved"))
