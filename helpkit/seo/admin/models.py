# coding=utf-8

from django.contrib import admin

from helpkit.common.admin.models import CommonModelAdmin
from helpkit.seo.models import Seo

__author__ = 'shade'


@admin.register(Seo)
class SeoAdmin(CommonModelAdmin):

    exclude = ('content_type', 'object_id', 'is_active',)
    list_display = ('id', 'uri', 'title',)