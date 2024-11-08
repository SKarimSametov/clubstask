from django.urls import path
from . import views
from .views import sing_up_page, login_page, logout_page, ClubForm

urlpatterns = [
    path('', views.test, name='main.urls'),
    path('jobs/', views.jobs_page, name='jobs_page'),
    path('categories/', views.categories_page, name='categories_page'),
    path('info/', views.full_info, name='full_info'),
    path('jobs/<int:pk>/', views.job_detail_page, name='job_detail_page'),
    path('categories/<slug:slug>/', views.jobs_by_category_page, name='jobs_by_category_page'),
    path('signup/', sing_up_page, name='signup_page'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),
    path('addclub/', ClubForm.as_view(), name='addclub'),
]