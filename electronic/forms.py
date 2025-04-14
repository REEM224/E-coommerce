from django import forms
from django.forms import ModelForm
from .models import product


class ProductForm(ModelForm):
    class Meta:
        model = product
        fields = ('name', 'color', 'price', 'quintity', 'tax', 'total', 'net')
     

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control from-control-sm'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control',}),
            'quintity': forms.NumberInput(attrs={'class': 'form-control'}),
            'tax': forms.NumberInput(attrs={'class': 'form-control'}),
            'total': forms.NumberInput(attrs={'class': 'form-control'}),
            'net': forms.NumberInput(attrs={'class': 'form-control'}),
        }