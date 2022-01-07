from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm #need to customize these for our use
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm): #using meta class to override existing fields
        model = CustomUser
        fields = ('username', 'email', 'age', 'is_host') #controls what we will see in signup form


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username', 'email', 'age')
