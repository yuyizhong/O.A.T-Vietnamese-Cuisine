from django.urls import path
from . import views


urlpatterns = [
    # Other URL patterns  
    path('reply/<int:pk>/', views.reply, name='reply'),    
]