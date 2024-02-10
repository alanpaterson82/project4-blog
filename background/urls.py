from . import views
from django.urls import path

urlpatterns = [
    path('', views.background_info, name='background'),
]