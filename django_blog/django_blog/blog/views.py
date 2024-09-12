from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, UserProfileForm
from .models import UserProfile


def home(request):
    return render(request, 'home.html', {})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('profile')
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid credentials'})
    return render(request, 'registration/login.html')

def logout(request):
    auth_logout(request)
    return redirect('home')

@login_required
def profile_view(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = CustomUserCreationForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)
    
    return render(request, 'blog/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
