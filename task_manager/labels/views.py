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
    """
        Create label view.
        Render a create label template.
        GET - create form
        POST - add data to DB(Label model)
        Redirect a user to labels page after successful creation.
        Return success message.
        Availiable only for logged users.
    """
    form_class = LabelForm
    form_class.base_fields['name'].label = _('Name')
    template_name = 'labels/create.html'
    success_url = reverse_lazy('labels')
    success_message = _('Label created successfully')


class UpdateLabel(CustomLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
        Update label view.
        Render a update label template.
        GET - update form
        POST - update data at DB(Label model)
        Redirect a user to labels page after successful update.
        Return success message.
        Availiable only for logged users.
    """
    model = Label
    form_class = LabelForm
    template_name = 'labels/update.html'
    success_url = reverse_lazy('labels')
    success_message = _('Label updated successfully')


class DeleteLabel(CustomLoginRequiredMixin, DeleteView):
    """
        Label delete view.
        Render a delete temlate for user.
        GET - ask user about the delete action.
        POST - delete label from DB(Label model).
        Return success message or error message.
        Availiable only for logged users.
    """
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
