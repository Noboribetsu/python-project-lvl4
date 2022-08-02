from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import ProtectedError
from task_manager.labels.models import Label
from django.http import HttpResponseRedirect
from task_manager.labels.forms import LabelForm
from django.utils.translation import gettext as _
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.labels.mixins import CustomLoginRequiredMixin


class LabelsList(CustomLoginRequiredMixin, ListView):
    """
        View return a list of all exist labels.
        Availiable only for logged users.
    """
    model = Label
    template_name = 'labels/labels.html'


class CreateLabel(CustomLoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = LabelForm
    form_class.base_fields['name'].label = _('Name')
    template_name = 'labels/create.html'
    success_url = reverse_lazy('labels')
    success_message = _('Label created successfully')


class UpdateLabel(CustomLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/update.html'
    success_url = reverse_lazy('labels')
    success_message = _('Label updated successfully')


class DeleteLabel(CustomLoginRequiredMixin, DeleteView):
    model = Label
    template_name = 'labels/delete.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        url = reverse_lazy('labels')
        try:
            self.object.delete()
            messages.add_message(request, messages.SUCCESS, _('Label deleted successfully'))
        except ProtectedError:
            messages.add_message(request, messages.ERROR, _('Not possible to delete a used label'))
            return HttpResponseRedirect(url)
        return HttpResponseRedirect(url)
