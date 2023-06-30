from django import forms
from .models import Review
from menu.models import MenuItem


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

def __init__(self, *args, **kwargs):
    # review_item = kwargs.pop('pk')
    super(ReviewForm, self).__init__(*args, **kwargs)
    # self.fields['menu_item'].queryset = MenuItem.objects.get( id=review_item)
        