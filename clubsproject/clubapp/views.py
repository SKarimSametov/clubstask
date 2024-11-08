from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, ClubModels
# # Create your views here.
from django.contrib.auth import login, authenticate, logout
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm

def test(request):
    categories = Category.objects.all()
    clubs = ClubModels.objects.all().order_by('-date')
    context = {
        'categories': categories,
        'clubs': clubs,
    }
    return render(request, "mainpage.html", context)

#


def jobs_page(request):
    clubs = ClubModels.objects.all().order_by('-date')
    context = {
        'clubs': clubs
    }
    return render(request, 'jobs.html', context)



def categories_page(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'categories.html', context)



def full_info(request):
    return render(request, 'base.html')


# d

def job_detail_page(request, pk):
    club = get_object_or_404(ClubModels, pk=pk)
    context = {
        'club': club
    }
    return render(request, "job-detail.html", context)



def jobs_by_category_page(request, slug):
    category = get_object_or_404(Category, slug=slug)
    clubs = ClubModels.objects.filter(category=category)
    context = {
        'category': category,
        'clubs': clubs
    }
    return render(request, "jobs-by-category.html", context)


# def sing_up_page(request):
#     if request.method == "POST":
#         form = NewUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             return redirect('login_page')
#         else:
#             form = NewUserForm()
#             context = {
#                 'form': form
#             }
#             return render(request, 'sing-up.html', context)


def sing_up_page(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login_page')
    else:
        form = NewUserForm()

    context = {
        'form': form
    }
    return render(request, 'sing-up.html', context)


def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main.urls')  # Убедитесь, что имя 'main' совпадает с названием маршрута на главную
    else:
        form = AuthenticationForm()  # Пустая форма для GET-запроса

    context = {
        'form': form
    }
    return render(request, 'login.html', context)
def logout_page(request):
    logout(request)
    return redirect('main.urls')
