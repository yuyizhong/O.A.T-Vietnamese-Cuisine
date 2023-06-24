from django import forms
from .models import MenuItem


class MenuForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = [
            'name',
            'description',
            'price',
            'menu_image',
            'status',
            # 'category'
        ]
