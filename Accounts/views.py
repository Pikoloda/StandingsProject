from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.contrib.auth.views import LoginView
from .form import CustomAuthenticationForm, CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('seasons_teams')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return render(request, 'seasons_teams.html')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')


class CustomLoginView(LoginView):
    def form_valid(self, form):
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse('seasons_teams')


login_view = CustomLoginView.as_view()
