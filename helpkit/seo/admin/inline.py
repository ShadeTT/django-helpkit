# coding=utf-8
from django.contrib.contenttypes.admin import GenericTabularInline

from helpkit.seo.models import Seo

__author__ = 'shade'


class SeoInline(GenericTabularInline):
    model = Seo
    extra = 0
    max_num = 1
    exclude = ('uri',)
