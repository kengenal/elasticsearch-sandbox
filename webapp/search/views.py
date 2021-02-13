from django.http import HttpResponse
from .models import PypiPackage


def index(request):
    print(PypiPackage.objects.all())
    return HttpResponse("hello world")
