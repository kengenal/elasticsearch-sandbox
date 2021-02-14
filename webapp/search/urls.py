from django.urls import path

from .views import PypiPackageView


urlpatterns = [
    path("", PypiPackageView.as_view(), name='search')
]
