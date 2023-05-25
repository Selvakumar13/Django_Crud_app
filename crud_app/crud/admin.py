from django.contrib import admin
from .models import Task
from faker import Faker


class Taskadmin(admin.ModelAdmin):
    list_display=('name', 'status')
    list_filter=('status',)
    search_fields = ('name',)
    actions=['mark_as_completed','mark_as_pending']

    def mark_as_completed(self,request,queryset):
        for task in queryset:
            task.status='Completed'
            task.save()
    mark_as_completed.short_description="Mark selected task as complete"

    def mark_as_pending(self,request,queryset):
        for task in queryset:
            task.status='Pending'
            task.save()
    mark_as_pending.short_description='Mark selected tasks as pending'


admin.site.register(Task,Taskadmin)