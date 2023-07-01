from django.urls import path
from . import views
from review import views as review_views


urlpatterns = [
    # Other URL patterns
    path('menu-list/', views.menu_list, name='menu-list'),
    path('menu-list/<int:pk>/', views.single_menu, name='single-menu'),
    path('add-menu/', views.add_menu, name='add-menu'),
    path('edit-menu/<int:menu_item_id>/', views.edit_menu, name='edit-menu'),
    path('hide-menu/<int:menu_item_id>', views.hide_menu, name='hide-menu'),
    path('delete-menu/<int:menu_item_id>',
         views.delete_menu, name='delete-menu'),
    
    path('meun-list/<int:pk>/leave-review/', review_views.leave_review, name='leave-review'),
]
