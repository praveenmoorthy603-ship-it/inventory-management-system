# from django.forms import ModelForm
from django import forms
from .models import Product 

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        

        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'product_code': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'gst': forms.NumberInput(attrs={'class': 'form-control'}),
            'food_product': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            
            'picture': forms.FileInput(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
        }