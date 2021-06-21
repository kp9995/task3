from django import forms
from .models import Products, Images
from django.forms import inlineformset_factory


class ProductAddForm(forms.ModelForm):
    class Meta:
        model = Products
        # fields = ['name','description','price','category','thumbnail']
        fields = '__all__'
class ImageAddForm(forms.ModelForm):

    class Meta:
        model = Images
        fields = ['image_path','product']
        widgets = {
            'image_path':forms.ClearableFileInput(attrs={'multiple':True})}
