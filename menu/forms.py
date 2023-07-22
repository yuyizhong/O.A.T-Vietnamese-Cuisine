from django import forms

from .models import MenuItem


class MenuForm(forms.ModelForm):
    """Form to add and edit menu contents"""
    class Meta:
        model = MenuItem
        fields = [
            'name',
            'description',
            'price',
            'menu_image',
            'status',
            'category'
        ]
