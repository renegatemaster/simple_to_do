from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TaskForm
from .models import Task


# @login_required(redirect_field_name='tasks:signup')
def index(request):
    template = 'tasks/index.html'
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
    }
    return render(request, template, context)


def add_task(request):
    template = 'tasks/add_task.html'
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            return redirect('tasks:index')
    form = TaskForm()
    context = {
        'form': form,
    }
    return render(request, template_name=template, context=context)


def task_detail(request, pk):
    template = 'tasks/task_detail.html'
    task = get_object_or_404(Task, id=pk, author=request.user)
    context = {
        'task': task,
    }
    return render(request, template, context)
