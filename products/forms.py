from django import forms
from .models import Products, Images


# class ProductAddForm(forms.ModelForm):
#     class Meta:
#         model = Products
#         fields = ['name','description','price','category']
#
# class ImageAddForm(forms.ModelForm):
#     class Meta:
#         model = Images
#         fields = ['image_path','product']
#         widgets = {
#             'products': forms.HiddenInput}

