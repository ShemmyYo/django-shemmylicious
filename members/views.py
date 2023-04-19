from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.urls import reverse_lazy
from django import forms
from .forms import SignUpForm, EditProfileForm, ProfilePageForm
from blog.models import Profile


# Profile Page Edit Pic, Bio & URL's
class CreateProfilePageView(generic.CreateView):
    model = Profile
    form = ProfilePageForm
    template_name = 'profile/create_profile.html'
    fields = ['bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url', 'pintrest_url']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# Profile Page Edit Settings 
class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'profile/user_profile_edit.html'
    success_url = reverse_lazy('edit-profile')

    fields = ['bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url', 'pintrest_url' ]

    widgets = {
        'profile_pic': forms.FileInput(attrs={
            'class': "form-control, fileInput, fileUpload, ",
            'type': "file"
            }),
        }


# Profile Page View
class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'profile/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user

        return context


# User Login
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None: 
            login(request, user)
            messages.success(request, "Successfully logged in. Welcome to your profile.")
            return redirect('my-profile')
        else:
            messages.success(request, "There was an error logging in")
            return redirect('login')


# User Registration
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')


# Edit Profile
class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('edit-profile')

    def get_object(self):
        return self.request.user


# Logout
def logout_user(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('start')
    

# Password Change
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('edit-profile')

