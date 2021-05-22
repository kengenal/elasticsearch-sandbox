from django.conf import settings
from django.core import serializers
from django.http import JsonResponse
from django.views.generic.base import View
from django.views.generic.list import MultipleObjectMixin
from django_elasticsearch_dsl.search import Search

from search.documents import PypiPackageDocument
from search.models import PypiPackage
from search.views import BasePypiQueryset


def prepare(data):
    res = []
    for inx, i in enumerate(data):
        res.append({
            "model": "search.pypipackage",
            "pk": inx,
            "fields": {
                "title": i.title,
                "author": i.author,
                "description": i.description,
                "link": i.link,
                "version": i.version,
                "authors": i.authors
            }
        })
    return res


class ApiPypiPackageView(BasePypiQueryset, MultipleObjectMixin, View):
    model = PypiPackage
    paginate_by = settings.PAGINATION
    document = PypiPackageDocument

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()

        if not allow_empty:
            if self.get_paginate_by(self.object_list) is not None and hasattr(self.object_list, 'exists'):
                is_empty = not self.object_list.exists()
            else:
                is_empty = not self.object_list
            if is_empty:
                return JsonResponse({"Error": "Not found"}, status=404)
        context = self.get_context_data().get("object_list", [])
        if isinstance(context, Search):
            js = prepare(context)
        else:
            js = serializers.serialize('python', context)
        return JsonResponse({"results": js}, status=200)
