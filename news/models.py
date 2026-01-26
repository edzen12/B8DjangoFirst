from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Category(models.Model):
    title = models.CharField(max_length=25, verbose_name="Название категории")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Категории'
        verbose_name = 'категория'

class News(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        null=True, verbose_name="Категория"
    )
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    description = CKEditor5Field('Описание', config_name='extends')
    image = models.ImageField(
        upload_to='newsMedia/', 
        verbose_name="Фотография поста"
    )
    public_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    update_date = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Новости'
        verbose_name = 'новость'


class Comment(models.Model):
    news = models.ForeignKey(
        News, on_delete=models.CASCADE, 
        related_name='comments'
    )
    name = models.CharField(max_length=50, verbose_name="Имя")
    text = models.TextField(verbose_name="Комментарии")
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} {self.text}"