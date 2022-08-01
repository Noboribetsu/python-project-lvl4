from django.urls import path
from task_manager.tasks.views import CreateTask, TasksList, UpdateTask, DeleteTask, DetailTask

urlpatterns = [
    path('tasks', TasksList.as_view(), name='tasks'),
    path('tasks/create', CreateTask.as_view(), name='create_task'),
    path('tasks/create/<int:pk>', DetailTask.as_view(), name='task_details'),
    path('tasks/<int:pk>/update', UpdateTask.as_view(), name='update_task'),
    path('tasks/<int:pk>/delete', DeleteTask.as_view(), name='delete_task'),
]
