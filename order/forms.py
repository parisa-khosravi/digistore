from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import *


class PaymentForm(forms.Form):
    amount=forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label='مبلغ',
        widget=forms.NumberInput(attrs={
            'class':'form-control','placeholder':'مبلغ مورد نظر'}
        )
    )
