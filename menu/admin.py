from django.contrib import admin
from .models import MenuItem, Category


@admin.register(MenuItem)
class MenuAdmin(admin.ModelAdmin):
    """ Class to display menu items on admin """
    list_display = (
        'menu_image',
        'name',
        'price',
        'category',        
    )
    list_filter = ('category', 'status')


admin.site.register(Category)
