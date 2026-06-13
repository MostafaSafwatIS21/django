from django.contrib import admin
from .models import Comment, Post, PostDetail, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content','image','created_at')
    search_fields = ('title', 'content')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created_at')
    search_fields = ('name', 'body')
    list_filter = ('created_at',)


@admin.register(PostDetail)
class PostDetailAdmin(admin.ModelAdmin):
    list_display = ('post', 'reading_time', 'source')
    search_fields = ('post__title', 'source')
