# coding=utf-8
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

__author__ = 'shade'


class SortableModel(models.Model):

    class Meta:
        abstract = True

    sort_index = models.PositiveSmallIntegerField(verbose_name='Сортировка', default=0)
    sort_index.help_text = 'Чем выше значение, тем выше элемент в сортировке'


class CommonModel(models.Model):

    class Meta:
        abstract = True

    created = models.DateTimeField('Дата добавления', auto_now_add=True)
    ts = models.DateTimeField('Дата изменения', auto_now=True)
    is_active = models.BooleanField(verbose_name='Активный', default=True)


class ImageModel(SortableModel, CommonModel):

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ('-is_cover', '-sort_index', '-created')
        app_label = 'common'

    image = models.ImageField(upload_to='images')

    is_cover = models.BooleanField('Главное', default=False)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
