from django.urls import path
from . import views


urlpatterns = [
    # Other URL patterns
    path('menu-list/', views.menu_list, name='menu-list'),
    path('add-menu/', views.add_menu, name='add-menu'),
    path('edit-menu/<int:menu_item_id>/', views.edit_menu, name='edit-menu'),
    # path('hide-menu/<menu_item_id>', views.hide_menu, name='hide-menu'),
    # path('delete-menu/<menu_item_id>',
    #      views.delete_menu, name = 'delete-menu'),
]
