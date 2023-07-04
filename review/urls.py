from django.urls import path
from . import views


urlpatterns = [
    # Other URL patterns
    path('reviews/', views.review_list, name='reviews'),
    path('item-reviews/<int:menu_id>/', views.item_reviews, name='item-reviews'),
    path('leave-review/<int:pk>/', views.leave_review, name='leave-review'),    
]
