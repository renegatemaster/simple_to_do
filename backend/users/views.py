from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import SignUpForm


class SignUp(CreateView):
    form = SignUpForm
    success_url = reverse_lazy('tasks:index')
    template_name = 'users/signup.html'
