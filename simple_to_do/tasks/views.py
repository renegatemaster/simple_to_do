from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import Task
from .forms import TaskForm


def index(request):
    template = 'tasks/index.html'
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
    }
    return render(request, template, context)


class AddTask(CreateView):
    queryset = Task.objects.all()
    form = TaskForm
    success_url = reverse_lazy('tasks:add_task')
    template_name = 'tasks/add_task.html'


def task_detail(request, pk):
    template = 'tasks/task_detail.html'
    task = Task.objects.get(pk=pk)
    context = {
        'task': task
    }
    return render(request, template, context)
