from django.urls import path

from users.views import SignUp

from .views import add_task, index, task_detail


app_name = 'tasks'


urlpatterns = [
    path('', index, name='index'),
    path('sigup/', SignUp.as_view(), name='signup'),
    path('add_task/', add_task, name='add_task'),
    path('task/<int:pk>/', task_detail, name='task_detail'),
]
