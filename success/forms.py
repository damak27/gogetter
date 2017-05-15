from django.contrib.auth.models import User
#from  success.models import UserProfile
from django import forms
from .models import UserProfile
class Creat_account(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields =['username','email','password','first_name','last_name']
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude=('user')
        fields =('bio','picture','company','field')