from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserRegisterForm(UserCreationForm):
  first_name = forms.CharField(widget = forms.TextInput(attrs = {'required': True}))
  last_name = forms.CharField(widget = forms.TextInput(attrs = {'required': True}))
  email = forms.CharField(label = 'Email address', widget = forms.TextInput(attrs = {'required': True}))
  
  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']

class UserUpdateForm(UserChangeForm):
  password = None
  
  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']