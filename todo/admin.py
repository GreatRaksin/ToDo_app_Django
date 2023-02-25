from django.contrib import admin
from .models import Task, Priority


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'priority', 'user_id', 'deadline_date',]
    list_filter = ['priority', 'status', 'user_id',]


class PriorityAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Task, TaskAdmin)
admin.site.register(Priority, PriorityAdmin)

