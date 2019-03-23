from django import forms
from .models import Profile, Business, Neighborhood, Post, Comment

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
