# forms.py
from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'category', 'purchase_date', 'notes']

        widgets = {
            'purchase_date': forms.DateInput(attrs={'type': 'date'}),
        }