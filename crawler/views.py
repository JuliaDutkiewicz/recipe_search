# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import shutil

from django.shortcuts import render

import requests


# Create your views here.


def index(request):
    meals = []
    for i in range(5):
        random_meal = requests.get('https://www.themealdb.com/api/json/v1/1/random.php')
        if (random_meal.status_code == 200):
            meals.append(random_meal.json()['meals'][0])
    first_recipe = requests.get('https://www.themealdb.com/api/json/v1/1/random.php')
    if (first_recipe.status_code != 200):
        first_recipe = None
    context = {
        'first_recipe': first_recipe.json()['meals'][0],
        'recipes': meals
    }
    return render(request, 'index.html', context)


def sign_in(request):
    return render(request, 'sign_in.html')


def log_in(request):
    return render(request, 'log_in.html')


def search(request):
    return render(request, 'search.html')


def favorites(request):
    return render(request, 'favorites.html')
