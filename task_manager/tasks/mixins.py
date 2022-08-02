from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from task_manager.tasks.models import Task
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin


class CustomLoginRequiredMixin(LoginRequiredMixin):
    """
        Login required check.
        Redirect not logged user to login page and
        return an error message.
    """
    login_url = reverse_lazy('login')
    redirect_field_name = None

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            messages.add_message(
                self.request, messages.ERROR,
                _('You are not logged in! Please log in.'))
        return super().handle_no_permission()


class TaskCheckOnDeleteMixin(UserPassesTestMixin, SuccessMessageMixin):
    """
        Task check on delete action Mixin:
        Only author is able to delete his task.
    """
    def test_func(self):
        task = Task.objects.get(id=self.kwargs['pk'])
        if task.author_id == self.request.user.id:
            return True
        self.login_url = reverse_lazy('tasks')
        messages.add_message(
            self.request, messages.ERROR,
            _('Only an author is able to delete a task'))
        return False

    def handle_no_permission(self):
        return redirect(self.login_url)
