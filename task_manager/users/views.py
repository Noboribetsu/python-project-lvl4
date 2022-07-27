
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from django.contrib.auth.models import User
from task_manager.users.forms import CustomUserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages


class CreateUser(SuccessMessageMixin, CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')
    success_message = _("User was registred successfully")


class AuthUser(SuccessMessageMixin, LoginView):
    model = User
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    next_page = reverse_lazy('index_page')
    success_message = _("You log in successfully")


class LogOutUser(LogoutView):
    model = User
    next_page = reverse_lazy('index_page')

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.SUCCESS, _('Successfully logged out.'))
        return response
