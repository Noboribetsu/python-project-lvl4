from django.db import models


class Task(models.Model):
    """
        Task model class.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    status = models.ForeignKey(
        'statuses.Status',
        on_delete=models.PROTECT,
        related_name='status')
    executor = models.ForeignKey(
        'auth.User',
        on_delete=models.PROTECT,
        related_name='executor', blank=True, null=True)
    labels = models.ManyToManyField(
        'labels.Label', through='TaskLabels',
        through_fields=('task', 'label'), blank=True,
        related_name='labels')
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.PROTECT,
        related_name='author')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TaskLabels(models.Model):
    """
        Task label model for m2m relations.
    """
    task = models.ForeignKey('tasks.Task', on_delete=models.PROTECT)
    label = models.ForeignKey('labels.Label', on_delete=models.PROTECT)
