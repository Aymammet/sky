from django import forms
from profiles.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name','email', 'password')
