from django import forms
from .models import Reply
from review.models import Review


class ReplyForm(forms.ModelForm):
    """
    Form for staff to reply a user's review
    """
    class Meta:
        model = Reply
        fields = [           
            'user',
            'content',
            'created_at',                      
        ]
