from django.shortcuts import redirect, get_object_or_404
from django.views import generic
from django.views.generic import DetailView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm
from blog.models import Profile


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'profile/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user

        return context


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None: 
            login(request, user)
            messages.success(request, (f"Successfully logged in. Welcome to your profile page {{ user }}"))
            return redirect('my-profile')
        else:
            messages.success(request, ("There was an error logging in"))
            return redirect('login')


def logout_user(request):
    logout(request)
    messages.success(request, ("Successfully logged out"))
    return redirect('start')
    

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('edit-profile')


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('edit-profile')

    def get_object(self):
        return self.request.user
