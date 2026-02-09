from django.contrib import admin
from apps.news.models import News, Category, Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'public_date', 'slug']
    prepopulated_fields =  {"slug": ["title",]}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields =  {"slug": ["title",]}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['news', 'is_published', 'created_at']
    list_filter = ('is_published',)
    list_editable = ('is_published',)
 
