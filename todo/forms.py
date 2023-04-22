from django import forms
from django.forms import DateInput
from .models import TasksList, Task


class TodoListForm(forms.ModelForm):
    class Meta:
        model = TasksList
        fields = ['title',]


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'due_date', 'status']
        widgets = {
            'due_date': DateInput(attrs={'type': 'date'})
        }
