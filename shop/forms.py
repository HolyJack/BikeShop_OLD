from django.db import models
from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    name = forms.CharField(label='your name', max_length=255)
    surname = forms.CharField(label='your surname', max_length=255)
    phone_number = forms.CharField(label='your phone number', max_length=255)

    class Meta:
        model = Order
        fields = ['name', 'surname', 'phone_number']


