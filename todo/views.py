from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import TasksList, Task, Priority
from .forms import TodoListForm, TaskForm, FeedbackForm
from transliterate import translit
import datetime


# Create your views here.
def index(request):
    form = FeedbackForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'index.html', {'title': 'ToDo App', 'form': form})


@login_required(login_url='/login')
def todo_lists(request):
    current_user = request.user  # фиксируем пользователя, который залогинился на сайте
    todo_list = TasksList.objects.filter(user=current_user)
    return render(request, 'todo_lists.html', {'lists': todo_list})


def create_list(request):
    user = request.user  # фиксирую пользователя, который сейчас работает со страницей
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            # сохраним новый список дел в базу данных
            todo_list = form.save(commit=False)
            todo_list.user = user
            todo_list.created_at = datetime.datetime.now()
            todo_list.save()
            return redirect('lists')
    else:
        form = TodoListForm()
    return render(request, 'form.html', {'form': form, 'title': 'New ToDo list'})


def show_list(request, title):
    task_list = get_object_or_404(TasksList, title=title)
    todos = Task.objects.filter(todo_list=task_list, status=False)
    now = datetime.datetime.now()  # фиксируем дату в тот момент, когда пользователь вошел на сайт
    return render(request, 'list_detail.html', {'todos': todos,
                                                'list_name': task_list.title,
                                                'today': now})


def complete_task(request, task_title):
    todo = get_object_or_404(Task, title=task_title)
    todo.status = True
    todo.save()
    list_title = todo.todo_list.title
    messages.success(request, f'Task "{task_title}" has been completed!')
    return redirect('current_list', title=list_title)


def edit_task(request, task_title):
    todo = get_object_or_404(Task, title=task_title)
    form = TaskForm(request.POST or None, instance=todo)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(reverse('current_list', args=[todo.todo_list.title]))
    return render(request, 'task_form.html', {'task': todo, 'title': f'Edit task "{task_title}"', 'form': form})


def delete_list(request, title):
    task_list = get_object_or_404(TasksList, title=title)
    task_list.delete()
    return redirect('lists')


def add_task(request, list_name):
    todo_list = get_object_or_404(TasksList, title=list_name)
    form = TaskForm(request.POST)
    if form.is_valid():  # если дали данные из формы
        # создаем новую задачу
        task = form.save(commit=False)
        task.todo_list = todo_list
        task.save()
        return redirect(reverse('current_list', args=[todo_list.title]))
    return render(request, 'task_form.html', {'title': 'New Task', 'form': form})
