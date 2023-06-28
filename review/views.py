from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Review


def review_list(request):
    reviews = Review.objects.all()

    # # Set the number of items per page
    # items_per_page = 10

    # paginator = Paginator(reviews, items_per_page)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)

   
    
    paginate_by = 6
     context = {
        'reviews': review,
        
        # 'page_obj': page_obj,
    }


    return render(request, 'review/reviews.html', context)
