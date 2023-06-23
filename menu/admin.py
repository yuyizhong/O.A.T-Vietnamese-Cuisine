from django.contrib import admin
from .models import Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """ Class to display menu items on admin """
    list_display = (
        'name',
        'type',
        'price',
        'average_rating'
    )
    list_filter = ('type', 'status')
