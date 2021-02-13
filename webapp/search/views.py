from django.http import HttpResponse

from .documents import PypiPackageDocument


def index(request):
    s = PypiPackageDocument.search()
    for hit in s:
        print(
            "Car name : {}, description {}".format(hit.title, hit.description)
        )
    return HttpResponse("hello world")
