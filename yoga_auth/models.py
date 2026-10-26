from django.db import models
from django.contrib.auth.models import User

# Модель для тем форума
class Topic(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название темы")
    description = models.TextField(verbose_name="Описание темы", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"

# Модель для сообщений/комментариев внутри тем
class Comment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="comments", verbose_name="Тема")
    text = models.TextField(verbose_name="Текст сообщения")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата отправки")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")

    def __str__(self):
        return f"Комментарий от {self.author.username} к теме {self.topic.title}"
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

# 3. НОВАЯ МОДЕЛЬ ОБОРУДОВАНИЯ ДЛЯ ФИТНЕСА
class Equipment(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название оборудования")
    description = models.TextField(verbose_name="Описание товара")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена (руб.)")
    image_url = models.ImageField(upload_to='equipment/', blank=True, null=True, verbose_name="Изображение товара")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Оборудование"
        verbose_name_plural = "Оборудование"
# Create your models here.
