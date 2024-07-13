from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def api_overview(request):
    api_urls = {
        'Register': '/api/register/',
        'Login': '/api/login/',
        'Main': '/api/main/',
    }
    return JsonResponse(api_urls)
