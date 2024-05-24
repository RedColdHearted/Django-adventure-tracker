from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Note
from users.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'profile_image']

    profile_image = forms.ImageField(required=False)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class NoteCreateForm(forms.ModelForm):
    location = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Note
        fields = ['title', 'description', 'location', 'date']

class NoteUpdtateForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'description']