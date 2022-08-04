from django.urls import path
from task_manager.statuses.views import CreateStatus, DeleteStatus, StatusesList, UpdateStatus

urlpatterns = [
    path('statuses/', StatusesList.as_view(), name='statuses'),
    path('statuses/create/', CreateStatus.as_view(), name='create_status'),
    path('statuses/<int:pk>/update/', UpdateStatus.as_view(), name='update_status'),
    path('statuses/<int:pk>/delete/', DeleteStatus.as_view(), name='delete_status'),

]
