from django import forms
from django.forms import ModelForm
from task_manager.tasks.models import Task
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from django_filters import FilterSet, BooleanFilter, ModelChoiceFilter


class TaskForm(ModelForm):
    """
        A form for model Status.
    """
    class Meta:
        model = Task
        fields = ('name', 'description', 'status', 'executor', 'labels')


class TaskFilter(FilterSet):
    """
        Filters for a task page.
    """
    status = ModelChoiceFilter(label=_('Status'), queryset=Status.objects.all())
    executor = ModelChoiceFilter(label=_('Executor'), queryset=User.objects.all())
    label = ModelChoiceFilter(field_name='labels', label=_('Labels'), queryset=Label.objects.all())
    self_tasks = BooleanFilter(
        label=_('Only own tasks'),
        method='get_own_tasks', widget=forms.CheckboxInput)

    def get_own_tasks(self, queryset, _, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset.all()
