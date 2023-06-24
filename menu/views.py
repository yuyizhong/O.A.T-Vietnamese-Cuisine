from django.shortcuts import render, get_object_or_404, redirect
# from .forms import ReviewForm
from .models import MenuItem, Category  # Add import for Category model
from .forms import MenuForm


def menu_list(request):
    menu_items_by_category = {}  # Dictionary to store menu items by category

    # Retrieve all menu items and group them by category
    categories = Category.objects.all()
    for category in categories:
        # Retrieve approved menu items for the category
        menu_items = MenuItem.objects.filter(
            category='category',
            status='approved'
        )
        menu_items_by_category[category] = menu_items

    context = {'menu_items_by_category': menu_items_by_category}
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


def edit_menu(request, item_id):
    item = get_pbject_or_404(MenuItem, id=item_id)
    form = MenuForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'menu/edit_menu.html', context)
