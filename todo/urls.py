from django.urls import path
from . import views  # из той же папки импортируем файл views


urlpatterns = [
    path('', views.index, name='index'),
    path('lists/', views.todo_lists, name='lists'),  # полный список всех туду-листов пользователя
    path('new_list/', views.create_list, name='new_list'),  # страница создания новго списка дел
    path('list/<str:title>', views.show_list, name='current_list'),  # страница с задачами из списка дел
    path('delete/<str:title>', views.delete_list, name='delete_list'),  # удаление списка дел
    path('new_task/<str:list_name>', views.add_task, name='add_task'),  # добавление задачи
    path('tasks/<str:task_title>/completed', views.complete_task, name='complete_task'),
    #path('tasks/<str:task_title>/edit', views.edit_task, name='edit_task'),
]
