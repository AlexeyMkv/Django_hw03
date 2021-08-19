from django.db import models


# Create your models here.
class Work(models.Model):
    organization = models.CharField(verbose_name='Организация', max_length=32)
    region = models.CharField(verbose_name='Регион', max_length=32, blank=True)
    site = models.CharField(verbose_name='Сайт', max_length=64, blank=True)
    position = models.CharField(verbose_name='Должность', max_length=16)
    duties = models.TextField(verbose_name='Обязанности')
    period = models.PositiveIntegerField(verbose_name='Время работы', default=1)


class Hobby(models.Model):
    name = models.CharField(verbose_name='Название', max_length=32)
    priority = models.CharField(verbose_name='Приоритет', max_length=16)
    special_preparation = models.CharField(verbose_name='Специальная подготовка', max_length=32)


class Study(models.Model):
    name = models.CharField(verbose_name='Учебное заведение', max_length=32)
    type = models.CharField(verbose_name='Тип', max_length=64)
    study_from = models.DateField(verbose_name='Дата начала обучения')
    study_to = models.DateField(verbose_name='Дата окончания обучения')
    description = models.CharField(verbose_name='Описание', max_length=300)
