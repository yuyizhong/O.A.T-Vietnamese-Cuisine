from django.urls import path
from . import views


urlpatterns = [
    # Other URL patterns
    path('reviews/', views.review_list, name='reviews'),
    # path('leave-review/<int:menu_item_id>/', views.leave_review, name='leave-review'),
    
    # path('edit-menu/<int:menu_item_id>/', views.edit_menu, name='edit-menu'),
    # path('hide-menu/<int:menu_item_id>', views.hide_menu, name='hide-menu'),
    # path('delete-menu/<int:menu_item_id>',
    #      views.delete_menu, name='delete-menu'),
]
