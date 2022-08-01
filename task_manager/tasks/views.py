from task_manager.tasks.forms import TaskForm
from task_manager.tasks.models import Task
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.statuses.mixins import CustomLoginRequiredMixin


class TasksList(CustomLoginRequiredMixin, ListView):
    """
        View return list of all exist tasks.
        Availiable on for logged users.
    """
    model = Task
    template_name = 'tasks/tasks.html'


class CreateTask(CustomLoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
        Create task view.
        Render a create task template.
        GET - Create form
        POST - add data to DB(Task model)
        Redirect a user to tassk page after successful creation.
        Return success message.
        Availiable on for logged users.
    """
    template_name = 'tasks/create.html'
    form_class = TaskForm
    form_class.base_fields['name'].label = _('Name')
    form_class.base_fields['description'].label = _('Description')
    form_class.base_fields['status'].label = _('Status')
    form_class.base_fields['executor'].label = _('Executor')
    success_url = reverse_lazy('tasks')
    success_message = _('Task created successfully')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateTask(CustomLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
        Update task view.
        Render a create task template.
        GET - update form
        POST - update data at DB(Task model)
        Redirect a user to tasks page after successful update.
        Return success message.
        Availiable only for logged users.
    """
    model = Task
    template_name = 'tasks/update.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    success_message = _('Task updated successfully')


class DeleteTask(CustomLoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """
        User delete view.
        Render a delete temlate for user.
        GET - ask user about the delete action.
        POST - delete user from DB(User model).
        Check if user logged and if a user try to update his own details.
        Return success message or error message.
    """
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks')
    success_message = _("Task deleted successfully")


class DetailTask(CustomLoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/detail.html'
