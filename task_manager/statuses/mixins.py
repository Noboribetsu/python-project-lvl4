from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin


class CustomLoginRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy('login')
    redirect_field_name = None

    def handle_no_permission(self):
        messages.add_message(
            self.request, messages.ERROR, _(
                'You are not logged in! Please log in.'))
        return super().handle_no_permission()
