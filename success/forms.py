from django.contrib.auth.models import User
from django import forms
class Creat_account(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields =['username','email','password','first_name','last_name'] 