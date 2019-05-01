# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import shutil

from django.contrib.flatpages.models import FlatPage
from django.http import HttpResponse
from django.shortcuts import render

import requests
from django.template import loader

import configuration

# Create your views here.


def index(request):
    meals = []
    for i in range(5):
        random_meal = requests.get('https://www.themealdb.com/api/json/v2/' + configuration.API_KEY + '/random.php')
        if (random_meal.status_code == 200):
            meals.append(random_meal.json()['meals'][0])
    first_recipe = requests.get('https://www.themealdb.com/api/json/v2/' + configuration.API_KEY + '/random.php')
    if (first_recipe.status_code != 200):
        first_recipe = None
    context = {
        'first_recipe': first_recipe.json()['meals'][0],
        'recipes': meals
    }
    return render(request, 'index.html', context)


def recipe(request, recipe_id):
    meal = requests.get(
        'https://www.themealdb.com/api/json/v2/' + configuration.API_KEY + '/lookup.php?i=' + str(recipe_id))
    if meal.status_code == 200:
        address = meal.json()["meals"][0]['strYoutube']
        embed_address = address.replace("watch?v=", "embed/")
        context = {
            "meal": meal.json()["meals"][0],
            "yt_url": embed_address,
        }
        return render(request, 'recipe.html', context)
    return HttpResponse("No such recipe")


def sign_in(request):
    return render(request, 'sign_in.html')


def log_in(request):
    return render(request, 'log_in.html')


def search(request):
    if request.method == 'GET':
        print(request.GET)
        query = request.GET.get('q')

        print(query)

        if query is not None:
            print(query)
            return render(request, 'search.html')

        else:
            return render(request, 'search.html')

    else:
        return render(request, 'search.html')


def favorites(request):
    return render(request, 'favorites.html')


def search_results(request):
    if 'q' in request.GET:
        input = request.GET['q']
        print(input)
        meal = requests.get(
            'https://www.themealdb.com/api/json/v2/' + configuration.API_KEY + '/filter.php?i=' + input)
        if meal.status_code == 200:
            context = {
                "meals": meal.json()["meals"]
            }

            return render(request, "search_results.html", context)
        else:
            return HttpResponse(meal.status_code)
    else:
        message = 'You submitted an empty form.'
        return HttpResponse(message)
