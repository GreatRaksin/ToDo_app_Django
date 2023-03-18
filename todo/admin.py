from django.contrib import admin
from .models import Task, Priority, TasksList


# Register your models here.
class TasksListAdmin(admin.ModelAdmin):
    list_display = ['title',]
    list_filter = ['user',]


class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'status',]
    list_filter = ['priority', 'status',]


class PriorityAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Task, TaskAdmin)
admin.site.register(Priority, PriorityAdmin)
admin.site.register(TasksList, TasksListAdmin)

