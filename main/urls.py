# core/urls.py
from django.urls import path
from .views import APIRootView

urlpatterns = [
    path('api/', APIRootView.as_view(), name='api-root'),
]
