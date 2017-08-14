# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators import csrf
from django.shortcuts import render


def search(request) :
    request.encoding = 'utf-8'
    if 'q' in request.GET:
        message = '您的搜索内容为: ' + request.GET['q']
    else:
        message = '您提交的内容为空'
    return HttpResponse(message)


# 表单
def search_form(request):
    return render_to_response('search_form.html')


def search_post(request) :
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "search_post_form.html", ctx)


