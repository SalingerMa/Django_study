# -*- coding: utf-8 -*-

from django.shortcuts import render
from .config import *

def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    context['athlete_list'] = athlete_list
    context['rows'] = [1, 2]
    context['cols'] = [1,2,3]
    return render(request, 'hello.html', context)

