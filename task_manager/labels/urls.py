from django.urls import path
from task_manager.labels.views import LabelsList, CreateLabel, DeleteLabel, UpdateLabel

urlpatterns = [
    path('labels', LabelsList.as_view(), name='labels'),
    path('labels/create', CreateLabel.as_view(), name='create_label'),
    path('labels/<int:pk>/update', UpdateLabel.as_view(), name='update_label'),
    path('labels/<int:pk>/delete', DeleteLabel.as_view(), name='delete_label'),
]
