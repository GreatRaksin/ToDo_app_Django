from django import forms
from .models import TasksList, Task
from tinymce.widgets import TinyMCE


class TodoListForm(forms.ModelForm):
    class Meta:
        model = TasksList
        fields = ['title',]


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ('created_at', 'status', 'todo_list')
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Task name...'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'content': TinyMCE(attrs={'cols': 100, 'rows': 40}),
        }
