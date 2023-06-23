from django.contrib import admin
from .models import MenuItem


@admin.register(MenuItem)
class MenuAdmin(admin.ModelAdmin):
    """ Class to display menu items on admin """
    list_display = (
        'menu_image',
        'name',
        'category',
        'price',
        'average_rating'
    )
    list_filter = ('category', 'status')
