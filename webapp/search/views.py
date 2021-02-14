from django.conf import settings
from django.views.generic import ListView

from .documents import PypiPackageDocument
from .models import PypiPackage


class PypiPackageView(ListView):
    model = PypiPackage
    template_name = 'search/list.html'
    paginate_by = settings.PAGINATION
    document = PypiPackageDocument

    def get_queryset(self):
        fil = self.request.GET.get('filter')
        try:
            data = self.document.get_elastic_data(fil)
            if data.count() <= 0:
                data = self.model.get_db_data(fil)
            return data
        except Exception as err:
            print(err)
            return self.model.get_db_data(fil)
