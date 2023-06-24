from django.urls import path
from . import views


urlpatterns = [
    # Other URL patterns
    path('menu-list/', views.menu_list, name='menu-list'),
    path('add-menu/', views.add_menu, name='add-menu'),
    path('edit-menu/<item_id>', views.edit_menu, name='edit-menu'),
    path('toggle-menu/<item_id>', views.toggle_menu, name='toggle-menu'),
]
