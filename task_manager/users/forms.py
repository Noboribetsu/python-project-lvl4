from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    """
    Custom User Creation Form:
    Add two additional fields to form.
    Fields: first_name, last_name, username, password1, password2
    Use for creation & update views.
    """
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name') + UserCreationForm.Meta.fields
