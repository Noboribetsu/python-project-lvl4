from django.urls import path

from task_manager.users.views import CreateUser

urlpatterns = [
    path('create/', CreateUser.as_view(), name='create_user'),
]