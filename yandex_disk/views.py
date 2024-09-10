import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.core.cache import cache

TEMPLATE_FILES_LIST = 'files_list.html'

def files_list(request) -> HttpResponse:
    public_key = request.GET.get('public_key')
    if not public_key:
        return render(request, TEMPLATE_FILES_LIST, {'error': 'Данные не введены'})

    cache_key = f'file_list_{public_key}'
    cached_data = cache.get(cache_key)
    if cached_data:
        return render(request, TEMPLATE_FILES_LIST, {'items': cached_data})

    url = f'https://cloud-api.yandex.net/v1/disk/public/resources'
    params = {'public_key': public_key}
    response = requests.get(url, params=params)
    try:
        response.raise_for_status()
    except requests.HTTPError:
        return render(request, TEMPLATE_FILES_LIST, {'error': 'Невозможно получить файлы'})

    data = response.json()
    items = [data] if data.get('type') == 'file' else data['_embedded']['items']

    cache.set(cache_key, items, timeout=600)
    return render(request, TEMPLATE_FILES_LIST, {'items': items})



