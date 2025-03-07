from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegisterView, profile_view, notifications_view
from .api import UserListView, UserDetailView, UserNotificationsView

urlpatterns = [
    path('api/users/', UserListView.as_view(), name='api-users-list'),
    path('api/users/<int:pk>/', UserDetailView.as_view(), name='api-users-detail'),
    path('api/notifications/', UserNotificationsView.as_view(), name='api-user-notifications'),
    path('register/', RegisterView.as_view(), name='user-register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(), name='user-logout'),
    path('profile/', profile_view, name='user-profile'),
    path('notifications/', notifications_view, name='user-notifications'),
]
