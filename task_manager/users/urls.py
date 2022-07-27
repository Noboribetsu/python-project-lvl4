from django.urls import path

from task_manager.users.views import AuthUser, CreateUser, LogOutUser

urlpatterns = [
    path('create/', CreateUser.as_view(), name='create_user'),
    path('login/', AuthUser.as_view(), name='login'),
    path('logout/', LogOutUser.as_view(), name='logout'),
]
