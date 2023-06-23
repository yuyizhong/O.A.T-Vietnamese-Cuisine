from django.urls import path
from . import views


urlpatterns = [
    # Other URL patterns
    path('menu-list/', views.menu_list, name='menu-list'),

]
