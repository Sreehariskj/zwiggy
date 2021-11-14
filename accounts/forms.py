from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from .models import User

class UserForm(UserCreationForm):
    email = forms.EmailField()
    phone = forms.IntegerField()
    
    class Meta:
        model = User
        #fields = '__all__'
        fields = ['phone','name','email']


