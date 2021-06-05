from django.urls import path

from .api.views import ApiPypiPackageView
from .views import PypiPackageView

urlpatterns = [
    path("", PypiPackageView.as_view(), name='search'),
    path("api/search", ApiPypiPackageView.as_view(), name='api-search')
]
