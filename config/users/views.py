from django.shortcuts import render, redirect  
from django.contrib.auth.decorators import login_required

from .forms import RegistrationForm, UserProfileForm
from .models import UserProfile
from django.contrib.auth import login


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():  
            user = form.save()
            login(request, user)
            return redirect('home')

    else:
        form = RegistrationForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    profile = UserProfile.objects.get(user=request.user)
    return render(request, 'users/profile.html', {'profile': profile})


@login_required
def edit_profile(request):
    profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('users:profile')

    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'users/edit_profile.html', {'form': form})