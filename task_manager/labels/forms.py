from django.forms import ModelForm
from task_manager.labels.models import Label


class LabelForm(ModelForm):
    """
        A form for model Label.
    """
    class Meta:
        model = Label
        fields = ('name', )
