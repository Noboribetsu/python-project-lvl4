# Generated by Django 4.0.6 on 2022-08-02 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
        ('tasks', '0006_tasklabels_task_labels_tasklabels_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(blank=True, related_name='labels', through='tasks.TaskLabels', to='labels.label'),
        ),
    ]
