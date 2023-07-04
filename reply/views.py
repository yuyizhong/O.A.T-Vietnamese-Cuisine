from django.shortcuts import render, redirect
from .models import Reply
from review.models import Review
from .forms import ReplyForm

def leave_review(request, pk):

    review = Review.objects.get(id=pk)
    form = ReplyForm()

    if request.method == 'POST':
        form = ReplyForm(request.POST, request.FILES)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.user = request.user
          
            reply.review = review
            reply.save()
        return redirect('item-reviews') 

    context = {
        'form': form,
        'menu_id': menu.id,
        'review': review
    }

    return render(request, 'reply/reply.html', context)
