from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from blog.models import Profile
from cloudinary.models import CloudinaryField


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'})),
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'})),
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'})),

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'})),
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'})),
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'})),
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'})),

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
    
        def __init__(self, *args, **kwargs):
            super(EditProfileForm, self).__init__(*args, **kwargs)

            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['first_name'].widget.attrs['class'] = 'form-control'
            self.fields['last_name'].widget.attrs['class'] = 'form-control'
            self.fields['email'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password2'].widget.attrs['class'] = 'form-control'


class ProfilePageForm(forms.ModelForm):
    model = Profile
    fields = ('user', 'bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url', 'pintrest_url')
    widgets = {
        'bio': forms.Textarea(attrs={'class': 'form-control'}),
        'profile_pic': forms.FileInput(attrs={'class': "form-control", 'type': "file"}),
        'website_url': forms.TextInput(attrs={'class': 'form-control'}),
        'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
        'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
        'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
        'pintrest_url': forms.TextInput(attrs={'class': 'form-control'}),
    }
