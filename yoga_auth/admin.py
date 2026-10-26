from django.contrib import admin
from .models import Topic, Comment, Equipment

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('created_at', 'author')
    search_fields = ('title', 'description')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'topic', 'text', 'created_at')
    list_filter = ('created_at', 'author', 'topic')
    search_fields = ('text',)

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at',)