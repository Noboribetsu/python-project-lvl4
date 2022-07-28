from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin


class UserCheckActionMixin(UserPassesTestMixin, SuccessMessageMixin):
    """
        Custom User check action Mixin:
        Check if a user logged and
        if a user has a permission update&delete a user profile.
        By default a user can update&delete only his own profile.
        Return messages in case of success or fault.
    """
    def test_func(self):
        if self.request.user.is_authenticated:
            if self.kwargs['pk'] == self.request.user.pk:
                return True
            self.url = reverse_lazy('users')
            messages.add_message(
                self.request, messages.ERROR, _(
                    'You don\'t have a permission to update another user'))
            return False
        self.url = reverse_lazy('login')
        messages.add_message(
            self.request, messages.ERROR, _(
                'You are not logged in! Please log in.'))
        return False

    def handle_no_permission(self):
        return redirect(self.url)
