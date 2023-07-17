from django import forms
from .models import Review
from menu.models import MenuItem


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            # 'menu_item',
            'rating',
            'content',
            'image', 
            'visit_date',                      
        ]
        widgets = {
            'visit_date': forms.DateInput(attrs={'type': 'date'}),
        }
        