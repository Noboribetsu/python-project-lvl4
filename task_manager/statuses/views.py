from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status
from task_manager.statuses.mixins import CustomLoginRequiredMixin
from django.db.models import ProtectedError
from django.contrib import messages


class CreateStatus(CustomLoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
        Create status view.
        Render a create status template.
        GET - Create form
        POST - add data to DB(Status model)
        Redirect a user to statusess page after successful creation.
        Return success message.
        Availiable on for logged users.
    """
    template_name = 'statuses/create.html'
    form_class = StatusForm
    form_class.base_fields['name'].label = _('Name')
    success_url = reverse_lazy('statuses')
    success_message = _('Status created successfully')


class StatusesList(CustomLoginRequiredMixin, ListView):
    """
        View return list of all exist statuses.
        Availiable on for logged users.
    """
    model = Status
    template_name = 'statuses/statuses.html'


class UpdateStatus(CustomLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
        Update status view.
        Render a create status template.
        GET - update form
        POST - update data at DB(Status model)
        Redirect a user to statusess page after successful update.
        Return success message.
        Availiable on for logged users.
    """
    model = Status
    template_name = 'statuses/update.html'
    form_class = StatusForm
    success_url = reverse_lazy('statuses')
    success_message = _('Status updated successfully')


class DeleteStatus(CustomLoginRequiredMixin, DeleteView):
    """
        Delete status view.
        Render a create status template.
        GET - ask user about the delete action.
        POST - delete status from DB(Status model).
        Redirect a user to statusess page after successful delete.
        Return success message.
        Availiable on for logged users.
    """
    model = Status
    template_name = 'statuses/delete.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        url = reverse_lazy('statuses')
        try:
            self.object.delete()
            messages.add_message(request, messages.SUCCESS, _('Status delete successfully'))
        except ProtectedError:
            messages.add_message(request, messages.ERROR, _('Not possible to delete a used status'))
            return HttpResponseRedirect(url)
        return HttpResponseRedirect(url)
