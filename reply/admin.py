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
    # Filter by review, created_at
    list_filter = ('review','created_at')
    # Search on created_at and content
    search_fields = ('created_at', 'content')
