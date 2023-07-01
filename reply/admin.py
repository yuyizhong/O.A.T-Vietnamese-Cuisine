from django.contrib import admin
from .models import Reply


@admin.register(Reply)
class ReviewAdmin(admin.ModelAdmin):
    """ Class to display reply items on admin """
    list_display = (
        'review',
        'user',
        'content',
        'created_at',        
    )
    list_filter = ('-created_at')
    search_fields = ('created_at', 'content')
