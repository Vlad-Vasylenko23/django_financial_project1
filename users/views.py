from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import User  
from django.db import IntegrityError
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not email or not password:
            return render(request, 'users/register.html', {'error': 'Всі поля обов’язкові'})

        try:
            validate_email(email)
        except ValidationError:
            return render(request, 'users/register.html', {'error': 'Некоректний email'})

        if User.objects.filter(username=username).exists():
            return render(request, 'users/register.html', {'error': 'Користувач з таким логіном вже існує'})
        if User.objects.filter(email=email).exists():
            return render(request, 'users/register.html', {'error': 'Користувач з таким email вже існує'})

        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password  
            )
            return redirect('users:login')
        except IntegrityError:
            return render(request, 'users/register.html', {'error': 'Помилка при створенні користувача'})

    return render(request, 'users/register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('main:home') 
        else:
            return render(request, 'users/login.html', {'error': 'Невірний логін або пароль'})
    return render(request, 'users/login.html')



def user_logout(request):
    auth_logout(request)
    return redirect('users:login')


