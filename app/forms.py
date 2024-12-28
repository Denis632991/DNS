
from django import forms
from .models import Product, Sklad, Dostavka

class SearchForm(forms.Form):
    name = forms.CharField(label='Поиск товара', max_length=255)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'describe', 'price', 'number']

class SkladForm(forms.ModelForm):
    class Meta:
        model = Sklad
        fields = ['name', 'products']

class DostavkaForm(forms.ModelForm):
    class Meta:
        model = Dostavka
        fields = ['city', 'city_off', 'cost_of_dostavka']

