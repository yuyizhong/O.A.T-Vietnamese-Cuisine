from django.urls import path
from .views import Reply
app_name = 'reply'

urlpatterns = [
    # Other URL patterns
    path('reply/<int:pk>/', Reply, name='reply'),
]
