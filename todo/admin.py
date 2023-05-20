from django.contrib import admin
from .models import Task, Priority, TasksList, Feedback


# Register your models here.
class TasksListAdmin(admin.ModelAdmin):
    list_display = ['title',]
    list_filter = ['user',]


class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'status',]
    list_filter = ['priority', 'status',]

    fieldsets = (
        (None, {
            'fields': ('title', 'due_date', 'status', 'todo_list')
        }),
        ('Content', {
            'fields': ('priority', 'content')
        }),
    )
    '''Каждая секция имеет свой заголовок (или None, если он не нужен) и ассоциированный кортеж 
    полей в словарях. Порядок полей в кортеже = порядку появления полей на странице в админке '''


class PriorityAdmin(admin.ModelAdmin):
    list_display = ['name']


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['subject', 'email', 'status']
    list_filter = ['email', 'status']


admin.site.register(Task, TaskAdmin)
admin.site.register(Priority, PriorityAdmin)
admin.site.register(TasksList, TasksListAdmin)
admin.site.register(Feedback, FeedbackAdmin)

