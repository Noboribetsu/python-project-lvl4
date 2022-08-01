from django.forms import ModelForm
from task_manager.tasks.models import Task


class TaskForm(ModelForm):
    """
        A form for model Status.
    """
    class Meta:
        model = Task
        fields = ('name', 'description', 'status', 'executor')
