from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Review, MenuItem
from .forms import ReviewForm


def review_list(request):
    reviews = Review.objects.all()

    # # Set the number of items per page
    # items_per_page = 10

    # paginator = Paginator(reviews, items_per_page)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)

   
    
    paginate_by: 6
    context = {
        'reviews': reviews,
        
        # 'page_obj': page_obj,
    }


    return render(request, 'review/reviews.html', context)


def leave_review(request, menu_item_id):
    menu_item = get_object_or_404(MenuItem, id=menu_item_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.menu_item = menu_item
            review.save()
            return redirect('menu-list') 
    else:
        form = ReviewForm()

    context = {
        'form': form,
        'menu_item': menu_item,
    }

    return render(request, 'review/leave_review.html', context)