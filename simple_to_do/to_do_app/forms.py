from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime
from .models import Task


class TaskForm(forms.ModelForm):
    deadline = forms.SplitDateTimeField(widget=AdminSplitDateTime())

    class Meta:
        model = Task
        fields = (
            'name',
            'body',
            'deadline',
            'importance'
        )
