from django.contrib import admin
from .models import Post
@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_status = ('status','created','publish','author')
    search_fields = ('title', 'body')   # поле поиска
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'  # ссылки для навигации по датам
    ordering = ('status', 'publish')