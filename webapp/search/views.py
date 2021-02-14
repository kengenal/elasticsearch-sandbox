from django.conf import settings
from django.db.models import Q
from django.views.generic import ListView

from .models import PypiPackage


class PypiPackageView(ListView):
    model = PypiPackage
    template_name = 'search/list.html'
    paginate_by = settings.PAGINATION

    def get_queryset(self):
        if self.request.GET.get('filter'):
            fil = self.request.GET.get('filter')
            return self.model.objects.filter(
                Q(author__icontains=fil)
                | Q(version__icontains=fil)
                | Q(authors__icontains=fil)
                | Q(author__icontains=fil)
                | Q(title__icontains=fil)
            ).all()
        return self.model.objects.all()
