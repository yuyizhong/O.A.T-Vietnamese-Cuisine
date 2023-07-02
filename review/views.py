from django.shortcuts import render, redirect, get_object_or_404, reverse
# from django.core.paginator import Paginator
from .models import Review
from menu.models import MenuItem, Category
from .forms import ReviewForm


def review_list(request):
    menu_id = request.GET.get('menu_id')
    if menu_id:
        reviews = Review.objects.filter(menu_item_id=menu_id)
    else:
        reviews = Review.objects.all()

    categories = Category.objects.all()

    context = {
        'reviews': reviews,
        'categories': categories,
    }

    return render(request, 'review/reviews.html', context)



def leave_review(request, pk):

    menu = MenuItem.objects.get(id=pk)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
          
            review.menu_item = menu
            review.save()
        return redirect('menu-list') 

    context = {
        'form': form,
        'menu_id': menu.id,
        'menu': menu
    }

    return render(request, 'review/leave_review.html', context)