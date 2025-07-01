# myphotos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('upload/', views.upload_photo, name='upload_photo'),
    path('logout/', views.user_logout, name='logout'),
]