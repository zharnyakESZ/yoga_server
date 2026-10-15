from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import YogaLoginForm

def yoga_login_view(request):
    # Если пользователь уже вошел в систему, сразу отправляем его на главную
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = YogaLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Проверяем, существует ли пользователь с таким логином и паролем
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)  # Авторизуем пользователя (создаем сессию)
                return redirect('home')  # Перенаправляем на главную страницу йоги
            else:
                # Если данные неверны, добавляем ошибку в форму
                form.add_error(None, "Неверное имя йогина или пароль")
    else:
        form = YogaLoginForm()
        
    return render(request, 'yoga_auth/login.html', {'form': form})

def home_view(request):
    return render(request, 'yoga_auth/joga.html')
