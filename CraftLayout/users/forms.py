from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class FormRegister(UserCreationForm):
    email = forms.EmailField(required=False)
    username = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['email']

class FirstProfileform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['position']
class SecondProfileform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']

class ProfileImage(forms.ModelForm):
    def __init__(self, *args, **kwards):
        super(ProfileImage, self).__init__(*args, **kwards)
        self.fields['Avatar'].label = "Изображение профиля"

    class Meta:
        model = Profile
        fields = ['Avatar']

class ProfileBanner(forms.ModelForm):
    def __init__(self, *args, **kwards):
        super(ProfileBanner, self).__init__(*args, **kwards)
        self.fields['banner'].label = "Баннер профиля"

    class Meta:
        model = Profile
        fields = ['banner']
