from django.urls import path
from django.contrib.auth import views as auth_views 
from .views import UserRegisterView, UserEditView, PasswordsChangeView
from .views import EditProfilePageView, CreateProfilePageView
from .views import ShowProfilePageView
from . import views


urlpatterns = [
    path('login/', views.login_user, name='login-user'),
    path('logout/', views.logout_user, name='logout-user'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show-profile'),
    path('<int:pk>/edit_profile/', EditProfilePageView.as_view(), name='edit-profile-page'),
    path('create_profile/', CreateProfilePageView.as_view(), name='create-profile-page'),
    path('edit_profile/', UserEditView.as_view(), name='edit-profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/password_change.html'), name='password'),
    
]
