from django.shortcuts import render
from .models import MenuItem


def menu_list(request):
    menu_items = MenuItem.objects.all().order_by('category')
    # categories = set(item.get_category_display() for item in menu_items)
    # categorized_menu = {}
    # for category in categories:
    #     categorized_menu[category] = [
    #         item for item in menu_items if item.get_category_display() == category]
    # context = {
    #     'categorized_menu': categorized_menu
    # }

    context = {
        'menu-items': menu_items
    }
    return render(request, 'menu_list.html', context)
