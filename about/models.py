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
    position = models.CharField(max_length=80, verbose_name="Должность")
    age = models.IntegerField(verbose_name="Возраст")
    experience=models.IntegerField(verbose_name="Стаж работы (лет)")

    def __str__(self):
        return f"{self.fullname} - {self.position}"
    
    class Meta:
        verbose_name_plural = 'Сотрудниках'