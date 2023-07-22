from django import forms
from .models import Review
from menu.models import MenuItem


class ReviewForm(forms.ModelForm):
    """
    Form to leave review
    """
    class Meta:
        model = Review
        fields = [
            # 'menu_item',
            'rating',
            'content',
            'image',
            'visit_date',
        ]
        # Define the visit_date format
        widgets = {
            'visit_date': forms.DateInput(attrs={'type': 'date'}),
        }
