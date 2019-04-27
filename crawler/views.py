# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from django.template import loader


# Create your views here.


def index(request):
    return render(request, 'index.html')


def sign_in(request):
    return render(request, 'working.html')


def log_in(request):
    return render(request, 'working.html')


def search(request):
    return render(request, 'working.html')


def favorites(request):
    return render(request, 'working.html')
