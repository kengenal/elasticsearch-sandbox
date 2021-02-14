from django.views.generic import ListView

from .models import PypiPackage


class PypiPackageView(ListView):
    model = PypiPackage
    template_name = 'search/list.html'
