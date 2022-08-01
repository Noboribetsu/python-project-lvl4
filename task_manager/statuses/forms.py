from django.forms import ModelForm
from task_manager.statuses.models import Status


class StatusForm(ModelForm):
    """
        A form for model Status.
    """
    class Meta:
        model = Status
        fields = ('name',)
