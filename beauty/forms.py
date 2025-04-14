from django import forms
from django.forms import ModelForm
from .models import product

class ProductForm(ModelForm):
    class Meta:
        model = product
        fields = ['name', 'color', 'price', 'quintity', 'tax', 'total', 'net']