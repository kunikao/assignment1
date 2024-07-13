from django.contrib import admin
from django.urls import path
from .views import index, api_overview

urlpatterns = [
    path('', index, name='index'),
    path('api/', api_overview, name='api-overview'),
]
