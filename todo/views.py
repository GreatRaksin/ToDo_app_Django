from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import TasksList, Task


# Create your views here.
def index(request):
    return render(request, 'index.html')


@login_required(login_url='/login')
def todo_lists(request):
    current_user = request.user  # фиксируем пользователя, который залогинился на сайте
    todo_list = TasksList.objects.filter(user=current_user)
    return render(request, 'todo_lists.html', {'lists': todo_list})


def create_list(request):
    pass


def show_list(request, title):
    task_list = get_object_or_404(TasksList, title=title)
    todos = Task.objects.filter(todo_list=task_list)
    return render(request, 'list_detail.html', {'todos': todos})
