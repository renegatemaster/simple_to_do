from django.urls import path

from .views import AddTask, index, task_detail

app_name = 'tasks'


urlpatterns = [
    path('', index, name='index'),
    path('add_task/', AddTask.as_view(), name='add_task'),
    path('task/<int:pk>/', task_detail, name='task_detail'),
]
