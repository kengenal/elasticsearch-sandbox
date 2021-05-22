from django.conf import settings
from django.views.generic import ListView

from .documents import PypiPackageDocument
from .models import PypiPackage


class BasePypiQueryset:
    request = None
    document = None
    model = None

    def get_queryset(self):
        fil = self.request.GET.get('filter')
        try:
            data = self.document.get_elastic_data(fil)
            if not data.count():
                data = self.model.get_db_data(fil)
            return data
        except Exception as err:
            print(err)
            return self.model.get_db_data(fil)


class PypiPackageView(BasePypiQueryset, ListView):
    model = PypiPackage
    template_name = 'search/list.html'
    paginate_by = settings.PAGINATION
    document = PypiPackageDocument

