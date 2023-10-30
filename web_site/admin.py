from django.contrib import admin
from .models import Category, Post, Profile, Comment

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')

class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'create_at', 'update_at', 'category')
    list_display_links = ('pk', 'title')

admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
