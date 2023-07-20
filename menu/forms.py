from django import forms

from .models import MenuItem

# Form to add and edit menu contents
class MenuForm(forms.ModelForm):
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
