# -*- coding: utf-8 -*-

from django.http import HttpResponse
from appModel.models import Test


def test_db(request):
    test1 = Test(name='jiang')
    test1.save()
    return HttpResponse(test1)


def update_db(request):
    test = Test.objects.filter(id=1)
    return HttpResponse(test)


def query_all(request):
    response = ""
    response1 = ""
    list_data = Test.objects.all()
    for var in list_data:
        response1 += var.name + "\r"
    response = response1
    return HttpResponse("<p>" + response + "</p>")

