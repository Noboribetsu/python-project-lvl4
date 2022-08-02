from task_manager.tasks.forms import TaskForm
from task_manager.tasks.models import Task
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.tasks.mixins import CustomLoginRequiredMixin, TaskCheckOnDeleteMixin


class TasksList(CustomLoginRequiredMixin, ListView):
    """
        View return a list of all exist tasks.
        Availiable only for logged users.
    """
    model = Task
    template_name = 'tasks/tasks.html'


class CreateTask(CustomLoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
        Create task view.
        Render a create task template.
        GET - create form
        POST - add data to DB(Task model)
        Redirect a user to tasks page after successful creation.
        Return success message.
        Availiable only for logged users.
    """
    template_name = 'tasks/create.html'
    form_class = TaskForm
    form_class.base_fields['name'].label = _('Name')
    form_class.base_fields['description'].label = _('Description')
    form_class.base_fields['status'].label = _('Status')
    form_class.base_fields['executor'].label = _('Executor')
    form_class.base_fields['labels'].label = _('Labels')
    success_url = reverse_lazy('tasks')
    success_message = _('Task created successfully')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateTask(CustomLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
        Update task view.
        Render a update task template.
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


class DeleteTask(CustomLoginRequiredMixin, TaskCheckOnDeleteMixin, DeleteView):
    """
        Task delete view.
        Render a delete temlate for user.
        GET - ask user about the delete action.
        POST - delete task from DB(Task model).
        Only author is able to delete a task.
        Availiable only for logged users.
        Return success message or error message.
    """
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks')
    success_message = _("Task deleted successfully")


class DetailTask(CustomLoginRequiredMixin, DetailView):
    """
        Task detail view.
        Render a detail page for user.
        With detailed information about a task.
        Availiable only for logged users.
    """
    model = Task
    template_name = 'tasks/detail.html'
