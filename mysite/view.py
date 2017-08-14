from django.shortcuts import render


def hello(request):
    context = {'hello': '少年强则中国强!'}
    return render(request, 'hello.html', context)
