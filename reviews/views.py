from django.shortcuts import render, redirect,get_object_or_404
from .models import Review
from .forms import ReviewForm

def review_list(request):
    #reviews = Review.objects.all(status=Review.Status.PUBLISHED)
    #reviews = get_object_or_404(status=Review.Status.PUBLISHED)
    reviews = Review.objects.filter(status=Review.Status.PUBLISHED)

    return render(request, 'reviews/review_list.html', {'reviews': reviews})

def add_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')
    else:
        form = ReviewForm()
    
    return render(request, 'reviews/add_review.html', {'form': form})
