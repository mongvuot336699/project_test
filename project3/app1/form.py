from django import forms
from .models import Product

class Product_form(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"