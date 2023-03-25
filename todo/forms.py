from django import forms
from .models import TasksList


class TodoListForm(forms.ModelForm):
    class Meta:
        model = TasksList
        fields = ['title',]

