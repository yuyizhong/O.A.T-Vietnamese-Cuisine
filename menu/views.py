from django.shortcuts import render
from .models import MenuItem
from .forms import MenuForm


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
    return render(request, 'menu/menu_list.html', context)

def add_menu(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    form = MenuForm()
    context = {
        'form': form
    }
    return render(request, 'menu/add_menu.html', context)