# coding=utf-8
from django.contrib.contenttypes.admin import GenericTabularInline

from helpkit.common.models import ImageModel

__author__ = 'shade'


class ImageInline(GenericTabularInline):
    model = ImageModel
    extra = 0
    exclude = ('is_active',)
