from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            'menu_item',
            'rating',
            'content',
            'image', 
            'visit_date',                      
        ]