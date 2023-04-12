from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', views.login_user, name='login-user'),
    path('logout/', views.logout_user, name='logout-user'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('<int:pk>/profile', ShowProfilePageView.as_view, name='show-profile'),
    path('edit_profile/', UserEditView.as_view(), name='edit-profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/password_change.html'), name='password'),
    
]
