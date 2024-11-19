from django.urls import path
from .views import index, stats

urlpatterns = [
    path('', index),
    path('stats/', stats)
]
