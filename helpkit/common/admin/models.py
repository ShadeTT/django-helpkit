# coding=utf-8

from django.contrib import admin

from helpkit.common.admin.inline import ImageInline
from helpkit.common.mixins import ImageMixin, SeoMixin
from django.db import models

from helpkit.seo.admin.inline import SeoInline

__author__ = 'shade'


class CommonModelAdmin(admin.ModelAdmin):

    save_as = True
    save_on_top = True
    date_hierarchy = 'created'

    def __init__(self, *args, **kwargs):

        search_fields = []

        super(CommonModelAdmin, self).__init__(*args, **kwargs)

        if issubclass(self.model, ImageMixin):
            self.inlines = list(self.inlines)
            self.inlines.insert(0, ImageInline)

        if issubclass(self.model, SeoMixin):
            self.inlines = list(self.inlines)
            self.inlines.insert(0, SeoInline)

        self.list_display_links = tuple(set(self.list_display) ^ set(self.list_editable))

        for field in self.model._meta.fields:
            if isinstance(field, (models.CharField, models.TextField)):
                search_fields.append(field.name)

        self.search_fields = list(self.search_fields) + search_fields


