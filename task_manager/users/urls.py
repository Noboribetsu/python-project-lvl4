from django.urls import path
from task_manager.users.views import AuthUser, CreateUser, LogOutUser, \
    UserDelete, UsersList, UserUpdate

urlpatterns = [
    path('users/', UsersList.as_view(), name='users'),
    path('users/<int:pk>/update/', UserUpdate.as_view(), name='update_user'),
    path('users/<int:pk>/delete/', UserDelete.as_view(), name='delete_user'),
    path('users/create/', CreateUser.as_view(), name='create_user'),
    path('login/', AuthUser.as_view(), name='login'),
    path('logout/', LogOutUser.as_view(), name='logout'),
]
