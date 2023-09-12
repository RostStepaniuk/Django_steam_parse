from django.shortcuts import render
from django.views.generic.base import View
from django.shortcuts import render
import pandas as pd
from django.conf import settings
import os
from django.http import JsonResponse
from . import scraper_steam_v2


def home_view(request):
    return render(request, 'steam1/steam.html')


def game_list_view(request):
    results = scraper_steam_v2.scrape_steam_data()
    print(results)
    return render(request, 'steam1/allgames2.html', {'games': results})


def test(request):
    data = {'a': 1, 'b': 2,'c':3 }
    print(data)
    return render(request, 'steam1/test.html', {'data': data})


def game_list_json(request):
    results = scraper_steam_v2.scrape_steam_data()
    return JsonResponse(results, safe=False)


