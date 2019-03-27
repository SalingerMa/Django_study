# -*- coding: utf-8 -*-

from django.shortcuts import render


def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    context['athlete_list'] = [{'name':'A'}, {'name': 'B'}, {'name': 'D'}]
    context['rows'] = [1, 2]
    context['cols'] = [1,2,3]
    return render(request, 'hello.html', context)

