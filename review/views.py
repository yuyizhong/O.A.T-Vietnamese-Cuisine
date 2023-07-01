from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.core.paginator import Paginator
from .models import Review
from menu.models import MenuItem
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


def leave_review(request, pk):
    menu = MenuItem.objects.get(id = pk)
  
    print(request)
    form = ReviewForm(instance=menu)

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=menu)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            print(request.user)
            # review.menu_item = menu_item
            review.save()
        return redirect('menu-list') 


    context = {
        'form': form,
        'menu': menu
    }

    return render(request, 'review/leave_review.html', context)