from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import TasksList, Task, Priority
from .forms import TodoListForm
import datetime


# Create your views here.
def index(request):
    return render(request, 'index.html')


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
    todos = Task.objects.filter(todo_list=task_list)
    return render(request, 'list_detail.html', {'todos': todos, 'list_name': task_list.title})


def delete_list(request, title):
    task_list = get_object_or_404(TasksList, title=title)
    task_list.delete()
    return redirect('lists')


def add_task(request, list_name):
    todo_list = get_object_or_404(TasksList, title=list_name)
    list_id = todo_list.id
    priorities = Priority.objects.all()
    if request.method == 'POST':  # если дали данные из формы
        title = request.POST['title']
        due_date = request.POST['due_date']
        content = request.POST['content']
        status = request.POST.get('status', False)
        priority = request.POST['priority']
        todo_list_id = list_id

        # создаем новую задачу
        task = Task.objects.create(title=title, due_date=due_date, content=content,
                                   status=status, priority=priority, todo_list=todo_list_id)
        task.save()
        return redirect('lists')
    return render(request, 'task_form.html', {'title': 'New Task', 'priorities': priorities})


def delete_task(request, task_id):
    pass
