from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    # Добавляем этот маршрут на первое место (пустые кавычки '' означают главную страницу)
    path('', views.home_view, name='home'),
    # Маршрут для страницы входа
    path('login/', views.yoga_login_view, name='login'),
    
    # Маршрут для выхода (после выхода перенаправит на логин)
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]