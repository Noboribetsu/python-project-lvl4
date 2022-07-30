from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status
from task_manager.statuses.mixins import CustomLoginRequiredMixin


class CreateStatus(CustomLoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'statuses/create.html'
    form_class = StatusForm
    form_class.base_fields['name'].label = _('Name')
    success_url = reverse_lazy('statuses')
    success_message = _('Status created successfully')


class StatusesList(CustomLoginRequiredMixin, ListView):
    model = Status
    template_name = 'statuses/statuses.html'


class UpdateStatus(CustomLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    template_name = 'statuses/update.html'
    form_class = StatusForm
    success_url = reverse_lazy('statuses')
    success_message = _('Status updated successfully')


class DeleteStatus(CustomLoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses')
    success_message = _('Status delete successfully')
