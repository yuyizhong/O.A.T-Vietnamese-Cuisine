from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """ Class to display review items on admin """
    list_display = (
        'menu_item',
        'user',
        'rating',
        'created_date',
        'content',
        'image',
        'visit_date'
    )
    list_filter = ('rating', 'user', 'created_date')
    search_fields = ('menu_item__name', 'user__username', 'content')

   