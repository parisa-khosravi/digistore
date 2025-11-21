from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['first_name','last_name','email','balance']
        labels={
            'first_name':'نام',
            'last_name':'نام خانوادگی',
            'email':'ایمیل',
            'balance':'اعتبار خرید',
        }
        widget={
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'last_name':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'balance':forms.NumberInput(attrs={'calss':'form-control'})
        }