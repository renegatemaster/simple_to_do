from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'body',
    )
    list_editable = ('name', 'body')
    search_fields = ('name', 'body')
    list_filter = ('created',)
    empty_value_display = 'Пусто (ツ)_/¯'
