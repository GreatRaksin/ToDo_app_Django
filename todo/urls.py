from django.urls import path
from . import views  # из той же папки импортируем файл views


urlpatterns = [
    path('', views.index, name='index'),
    path('lists/', views.todo_lists, name='lists'),  # полный список всех туду-листов пользователя
    path('new_list/', views.create_list, name='new_list'),  # страница создания новго списка дел
    path('list/<str:title>', views.show_list, name='current_list'),  # страница с задачами из списка дел
]
