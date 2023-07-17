from django.shortcuts import redirect, reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.exceptions import PermissionDenied


from .models import MenuItem, Category  # Add import for Category model
from .forms import MenuForm


def menu_list(request):
    if request.user.is_superuser:  # Check if user is an admin
        menu_items = MenuItem.objects.all()
    else:
        menu_items = MenuItem.objects.filter(status='approved')

    menu_items_by_category = {}  # Dictionary to store menu items by category

    # Retrieve all menu items and group them by category
    categories = Category.objects.all()
    for category in categories:
        category_menu_items = menu_items.filter(category=category)
        menu_items_by_category[category] = category_menu_items

    print(menu_items_by_category)

    context = {'menu_items_by_category': menu_items_by_category}
    return render(request, "menu/menu_list.html", context)


def add_menu(request):
    """ Create menu view to create a menu if user is staff """
    if not request.user.is_staff:
        raise PermissionDenied()

    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # flash message
            messages.success(request, 'Your menu is successfully added!')
            # Redirect to menu-list URL name
            return redirect('menu-list')
    form = MenuForm()
    context = {
        'form': form
    }
    return render(request, 'menu/add_menu.html', context)


def edit_menu(request, menu_item_id):
    item = get_object_or_404(MenuItem, id=menu_item_id)
    form = MenuForm(instance=item)

    """ Edit menu view to edit a menu if user is staff """
    if not request.user.is_staff:
        raise PermissionDenied()
        
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()
            # flash message
            messages.success(request, 'Your menu is successfully updated!')
            return redirect('menu-list')

    context = {
        'form': form
    }
    return render(request, 'menu/edit_menu.html', context)


def hide_menu(request, menu_item_id):
    menu_item = get_object_or_404(MenuItem, id=menu_item_id)
    if menu_item.status == 'approved':
        menu_item.status = 'hidden'
        # flash message
        messages.success(request, 'Your menu is now successfully hidden!')
    elif menu_item.status == 'hidden':
        menu_item.status = 'approved'
        # flash message
        messages.success(request, 'Your menu is now successfully unhidden!')
    menu_item.save()
    return redirect('menu-list')


def delete_menu(request, menu_item_id):
    menu_item = get_object_or_404(MenuItem, id=menu_item_id)
    menu_item.delete()
    # flash message
    messages.success(request, 'Your menu was successfully deleted!')
    return redirect('menu-list')
