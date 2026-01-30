from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class About(models.Model):
    title = models.CharField(
        verbose_name="Заголовок", max_length=150,
        help_text="О нас / О компании / Наша история"
    )
    description = CKEditor5Field('Описание', config_name='extends')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'О компании'

class Staff(models.Model):
    fullname = models.CharField(max_length=100, verbose_name="ФИО")
    image = models.ImageField(
        upload_to='staff/', verbose_name="Фото", null=True
    )
    position = models.CharField(max_length=80, verbose_name="Должность")
    age = models.IntegerField(verbose_name="Возраст")
    experience=models.IntegerField(verbose_name="Стаж работы (лет)")
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return f"{self.fullname} - {self.position}"
    
    class Meta:
        verbose_name_plural = 'Сотрудниках'


class SocialLink(models.Model):
    employee = models.ForeignKey(
        Staff, verbose_name="Сотрудник", on_delete=models.CASCADE
    )
    title = models.CharField(verbose_name="Название соцсети", max_length=30)
    link = models.CharField(verbose_name="ссылка на соцсеть", max_length=255)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Соцсети'
        verbose_name = 'соцсеть'

