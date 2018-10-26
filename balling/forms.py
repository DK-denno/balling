from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Message

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)
  

    class Meta:
        model = User
        exclude = []
        fields = ['first_name','last_name','username','email','password1','password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        fields = ['dp','bio']

class MessageForm(forms.ModelForm):
    message = forms.CharField()
    class Meta:
        model = Message
        exclude = []
        fields = ['message']

class ChangeLeagueForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['dp','bio','phone_number']
        fields = ['league']