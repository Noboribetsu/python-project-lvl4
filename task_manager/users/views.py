from django import urls
from django.shortcuts import redirect
from django.views.generic import TemplateView,CreateView
from django.contrib.auth.models import User
from task_manager.users.forms import CustomUserCreationForm


class CreateUser(CreateView):
    model = User
    form_class = CustomUserCreationForm
    #fields = ['first_name', 'last_name', 'username']
    template_name = 'users/create.html'
