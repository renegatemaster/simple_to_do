from django.shortcuts import render

from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks/index.html', context)


def add_task(request):
    form = TaskForm
    context = {
        'form': form
    }
    return render(request, 'tasks/add_task.html', context)
