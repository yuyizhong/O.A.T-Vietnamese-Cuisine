from django.shortcuts import render, redirect, get_object_or_404, reverse
# from django.core.paginator import Paginator
from .models import Review
from menu.models import MenuItem, Category
from .forms import ReviewForm


def review_list(request):    
    menuitems = MenuItem.objects.all()

    avg ={}
    for item in menuitems:
        avg[item.name] = Review.average_rating(item)
        print(avg[item.name])

    reviews = Review.objects.all()

    categories = Category.objects.all()

    context = {
        'reviews': reviews,
        'categories': categories,
        'menuitems': menuitems,
        'avg':avg, 
    }

    return render(request, 'review/reviews.html', context)
    

def item_reviews(request, menu_id):
    
    item = MenuItem.objects.get(id = menu_id)
   
    print(item.name)
    item_reviews = item.review_set.all()

    context = {
        'item_reviews': item_reviews,

    }

    return render(request, 'review/review_details.html', context)

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
        return redirect('item-reviews', menu_id=review.menu_item.id) 

    context = {
        'form': form,
        'menu_id': menu.id,
        'menu': menu
    }

    return render(request, 'review/leave_review.html', context)