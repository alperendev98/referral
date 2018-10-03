from django.contrib import admin

from referral_project.tasks.models import Task, TaskStatus, CustomTask, CustomTaskStatus
from referral_project.utils.django.admin import TimeStampedModelAdmin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

@admin.register(Task)
class TaskAdmin(TimeStampedModelAdmin):
    list_display = [
        'name',
        'kind',
        'link',
        'reward',
        'campaign',
        'status',
        'max_interactions',
        'expired',
    ]

    list_filter = [
        'kind'
    ]


@admin.register(TaskStatus)
class TaskStatusAdmin(TimeStampedModelAdmin):
    list_display = [
        'interacted',
    ]


@admin.register(CustomTask)
class CustomTaskAdmin(TimeStampedModelAdmin):
    list_display = [
        'title',
        'reward',
        'instruction',
        'campaign',
        'status',
        'max_interactions',
        'expired',
        'work_proof',
        'action',
    ]


@admin.register(CustomTaskStatus)
class CustomTaskStatusAdmin(TimeStampedModelAdmin):
    list_display = [
        'interacted'
    ]
    list_filter = [
        ('created', DateRangeFilter),
        ('modified', DateRangeFilter),
    ]
