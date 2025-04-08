from django.contrib.auth import views as auth_views
from django.urls import path
from user_management.views import CustomSignUpView  # Import your signup view

urlpatterns = [
    # Login
    path('login/', auth_views.LoginView.as_view(template_name='user_management/login.html'), name='login'),

    # Password Change
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='user_management/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='user_management/password_change_done.html'), name='password_change_done'),

    # Signup (registration)
    path('signup/', CustomSignUpView.as_view(), name='signup'),
]
