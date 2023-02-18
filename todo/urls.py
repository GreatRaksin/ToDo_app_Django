from django.urls import path
from . import views  # из той же папки импортируем файл views


urlpatterns = [
    path('', views.index, name='index'),
]
