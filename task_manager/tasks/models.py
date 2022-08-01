from django.db import models


class Task(models.Model):
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
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.PROTECT,
        related_name='author')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
