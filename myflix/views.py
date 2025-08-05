from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def users(request):
    if request.method == 'GET':
        user = {
            'id': 1,
            'name': 'Alexandre',
        }
        return JsonResponse(user, json_dumps_params={'ensure_ascii': False})
    return