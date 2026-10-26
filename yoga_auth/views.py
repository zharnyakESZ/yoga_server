from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import YogaLoginForm  # убедитесь, что имя файла формы совпадает
from .models import Topic, Comment, Equipment

def yoga_login_view(request):
    if request.user.is_authenticated:
        return redirect('joga')

    if request.method == 'POST':
        form = YogaLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('joga')
            else:
                form.add_error(None, "Неверное имя йогина или пароль")
    else:
        form = YogaLoginForm()
        
    return render(request, 'yoga_auth/login.html', {'form': form})

# Функция выхода из системы (добавлена)
def yoga_logout_view(request):
    logout(request)
    return redirect('joga')

def home_view(request):
    return render(request, 'yoga_auth/joga.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('joga')  # Сразу направляем на главную после создания аккаунта
    else:
        form = UserCreationForm()
    return render(request, 'yoga_auth/register.html', {'form': form})

# 1. СМОТРЕТЬ ВСЕ ТЕМЫ + СОЗДАНИЕ ТЕМЫ
def forum_view(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponseForbidden("Вам необходимо зарегистрироваться.")
        
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title:
            Topic.objects.create(title=title, description=description, author=request.user)
            return redirect('/users/forum/')
            
    topics = Topic.objects.all().order_by('-created_at')
    return render(request, 'yoga_auth/forum.html', {'topics': topics})

# 2. ПРОСМОТР ТЕМЫ + ДОБАВЛЕНИЕ КОММЕНТАРИЕВ
def topic_detail_view(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponseForbidden("Вам необходимо зарегистрироваться.")
            
        text = request.POST.get('text')
        if text:
            Comment.objects.create(topic=topic, text=text, author=request.user)
            return redirect(f'/users/forum/{topic.id}/')
            
    comments = topic.comments.all().order_by('created_at')
    return render(request, 'yoga_auth/topic_detail.html', {'topic': topic, 'comments': comments})

# 3. УДАЛЕНИЕ ТЕМЫ (Доступно только Администраторам)
def delete_topic_view(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    if request.user.is_authenticated and (request.user.is_superuser or request.user.is_staff):
        topic.delete()
        return redirect('/users/forum/')
    return HttpResponseForbidden("У вас недостаточно прав для удаления темы.")

# 4. УДАЛЕНИЕ КОММЕНТАРИЯ (Доступно только Администраторам)
def delete_comment_view(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    topic_id = comment.topic.id
    if request.user.is_authenticated and (request.user.is_superuser or request.user.is_staff):
        comment.delete()
        return redirect(f'/users/forum/{topic_id}/')
    return HttpResponseForbidden("У вас недостаточно прав для удаления комментария.")

# 5. РЕДАКТИРОВАНИЕ КОММЕНТАРИЯ (Доступно автору комментария и Администраторам)
def edit_comment_view(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    topic_id = comment.topic.id
    
    is_author = request.user == comment.author
    is_admin = request.user.is_superuser or request.user.is_staff
    
    if not request.user.is_authenticated or not (is_author or is_admin):
        return HttpResponseForbidden("У вас нет прав на редактирование этого сообщения.")
        
    if request.method == 'POST':
        new_text = request.POST.get('text')
        if new_text:
            comment.text = new_text
            comment.save()
            return redirect(f'/users/forum/{topic_id}/')
            
    return render(request, 'yoga_auth/edit_comment.html', {'comment': comment})

def yoga_logout_view(request):
    logout(request)
    return redirect('joga')  # или 'login', смотря куда хотите перенаправлять после выхода

def shop_view(request):
    items = Equipment.objects.all().order_by('-created_at')
    return render(request, 'yoga_auth/shop.html', {'items': items})
