from django.urls import path, include
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('login/', views.yoga_login_view, name='login'),
    path('logout/', views.yoga_logout_view, name='logout'),
    path('joga/', views.home_view, name='joga'),
    path('register/', views.register_view, name='register'),
    path('', RedirectView.as_view(url='joga/', permanent=True)),
    path('forum/', views.forum_view, name='forum'), # Теперь итоговый путь будет /users/forum/
    path('forum/<int:topic_id>/', views.topic_detail_view, name='topic_detail'),
    path('delete-topic/<int:topic_id>/', views.delete_topic_view, name='delete_topic'),
    path('delete-comment/<int:comment_id>/', views.delete_comment_view, name='delete_comment'),
    path('edit-comment/<int:comment_id>/', views.edit_comment_view, name='edit_comment'),
    path('shop/', views.shop_view, name='shop'),

]
