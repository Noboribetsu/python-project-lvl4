from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from task_manager.users.forms import CustomUserCreationForm
from task_manager.users.mixins import UserCheckActionMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView


class CreateUser(SuccessMessageMixin, CreateView):
    """
        Create user view.
        Use custom UserCreationFrom
        Render a login template for user.
        GET - Registration form
        POST - add data to DB(User model)
        Redirect a user to log in page after successful registration.
        Return success message after registration.
    """
    form_class = CustomUserCreationForm
    form_class.base_fields['first_name'].required = True
    form_class.base_fields['last_name'].required = True
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')
    success_message = _("User was registred successfully")



class AuthUser(SuccessMessageMixin, LoginView):
    """
        Authentication view.
        Use Django built-in form.
        Render a log in template for user.
        GET - log in form.
        POST - submit details
        Redirect a user to index page after successful login.
        Return success message.
    """
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    next_page = reverse_lazy('index_page')
    success_message = _("You log in successfully")


class LogOutUser(LogoutView):
    """
        Log out view.
        Redirect user to index page.
        Return success message.
    """
    next_page = reverse_lazy('index_page')

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.SUCCESS, _('Successfully logged out.'))
        return response


class UsersList(ListView):
    """
        User list view.
        Render a users template with a list of all users.
    """
    model = User
    template_name = 'users/users.html'


class UserUpdate(UserCheckActionMixin, UpdateView):
    """
        User update view.
        Render a update temlate for user.
        GET - a form with fields.
        POST - update details in DB(User model).
        Check if user logged and if a user try to update his own details.
        Return success message or error message.
    """
    model = User
    form_class = CustomUserCreationForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users')
    success_message = _("User updated successfully")


class UserDelete(UserCheckActionMixin, DeleteView):
    """
        User delete view.
        Render a delete temlate for user.
        GET - ask user about the delete action.
        POST - delete user from DB(User model).
        Check if user logged and if a user try to update his own details.
        Return success message or error message.
    """
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users')
    success_message = _("User deleted successfully")
