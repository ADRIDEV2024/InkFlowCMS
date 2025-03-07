from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .models import CustomUser, UserNotification
from .forms import UserRegisterForm, UserUpdateForm

class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
        return render(request, 'users/register.html', {'form': form})

@login_required
def profile_view(request):
    user = request.user
    form = UserUpdateForm(instance=user)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('profile')
    return render(request, 'users/profile.html', {'form': form})

@login_required
def notifications_view(request):
    notifications = UserNotification.objects.filter(user=request.user, is_read=False)
    return render(request, 'users/notifications.html', {'notifications': notifications})
