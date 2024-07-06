from django import forms
from .models import *
from django.forms import modelformset_factory

class PresentationForm(forms.ModelForm):
    class Meta:
        model = Presentation
        fields = ['name', 'description', 'status']
        #widgets = {"title": forms.TextInput(attrs={"class": "form-control inputs"}), "description": forms.Textarea(attrs={"class": "form-control inputs"}),"image": forms.FileInput(attrs={"class": "form-control-field inputs"}) }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['categoryname', 'status']

class SizeForm(forms.ModelForm):
    class Meta:
        model = Size
        fields = ['size', 'status']

class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = ['systemname', 'image', 'address', 'phone', 'exchange']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['size', 'productname', 'presentation', 'description', 'status']

# class SaleForm(forms.ModelForm):
#     class Meta:
#         model = Sale
#         fields = ['customer_name', 'sub_total', 'total', 'discount', 'user', 'money_r', 'money_change', 'code', 'status']

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'  

class SaleDetailForm(forms.ModelForm):
    class Meta:
        model = Sale_detail
        fields = '__all__' 

SaleDetailFormSet = modelformset_factory(Sale_detail, form=SaleDetailForm, extra=1)