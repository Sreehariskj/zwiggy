from django import forms
from accounts.models import User
from .models import Profile

class UpdateUserForm(forms.ModelForm):
    name = forms.CharField(max_length =100,
    required=True,widget= forms.TextInput(attrs ={'class':'form-control'}))
    email = forms.EmailField(required=True, widget= forms.EmailInput(attrs ={'class':'form-control'}))
    phone = forms.IntegerField(required=True,widget= forms.NumberInput(attrs ={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ['name','phone','email']


class UpdateProfileForm(forms.ModelForm):
    address = forms.CharField(max_length=250,widget= forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = Profile
        fields = ['address']