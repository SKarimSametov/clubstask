from django.shortcuts import render
from .models import Category, ClubModels
# Create your views here.


def test(request):
    categories = Category.objects.all()
    jobs = ClubModels.objects.all
    context = {
        'categories': categories,
        'jobs': jobs
    }
    return render(request, "./mainpage.html", context)