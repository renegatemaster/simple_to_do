from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import TaskForm
from .models import Task


def index(request):
    template = 'tasks/index.html'
    tasks = Task.objects.filter(user=request.user)
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
    task = get_object_or_404(Task, id=pk, user=request.user)
    context = {
        'task': task,
    }
    return render(request, template, context)
