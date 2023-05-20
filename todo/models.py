from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_models
from datetime import datetime


class Priority(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class TasksList(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название списка дел')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'список дел'
        verbose_name_plural = 'Списки дел'
        ordering = ('created_at',)  # сортировка


class Task(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    content = tinymce_models.HTMLField(max_length=7000)
    status = models.BooleanField(default=False)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE,
                                 default=None)
    todo_list = models.ForeignKey(TasksList, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Задачу'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.title


class Feedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __repr__(self):
        return self.name + ' ' + self.subject



