from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import *

class UserRegisterForm(UserCreationForm):
    phone=forms.CharField(
        label='شماره تلفن',
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    ROLE_CHOICES=[('customer','خریدار'),('seller','فروشنده')]
    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        label='نقش کاربر',
        widget=forms.Select(attrs={"class": "form-control"})
    )
    password1=forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={'class':'form-control'})
    )
    password2=forms.CharField(
        label='تایید رمزعبور',
        widget=forms.PasswordInput(attrs={'class':'form-control'})
    )
    class Meta:
        model=CustomUser
        fields=['phone','role','password1','password2']


    def save(self, commit =True):
        user=super().save(commit=False)
        user.username = self.cleaned_data['phone'] 
        role=self.cleaned_data.get('role')
        if role == 'seller':
            user.is_seller=True
            user.is_customer=False
        else:
            user.is_seller=False
            user.is_customer=True
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    username=forms.CharField(
        label='شماره تلفن',
        widget=forms.TextInput(attrs={'class':'form_control'})
    )
    password=forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={'class':'form_control'})
            
    )