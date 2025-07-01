from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from .forms import PhotoForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

# Create your views here.
def home(request):

    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in after registration
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

from .models import Photo

def profile(request):
    if request.user.is_authenticated:
        user_photos = Photo.objects.filter(uploaded_by=request.user)
        return render(request, 'profile.html', {'user': request.user, 'photos': user_photos})
    else:
        return redirect('login')


def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploaded_by = request.user
            photo.save()
            return redirect('profile')
    else:
        form = PhotoForm()
    return render(request, 'upload_photo.html', {'form': form})

def user_logout(request):
        logout(request)
        return redirect('home')
    
# @csrf_exempt
# def send_feedback(request):
#     if request.method == 'POST':
#         message = request.POST.get('message')
#         # You could process/save the message here
#         print("Feedback received:", message)  # or log it
#         messages.success(request, "Thank you for your feedback!")
#         return redirect('about')  # redirect back to About page

#     return redirect('about')