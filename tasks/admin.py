from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('owner', 'title', 'description', 'is_urgent',
                    'due_date', 'completed')


admin.site.register(Task, TaskAdmin)
