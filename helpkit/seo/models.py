# coding=utf-8

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _

from helpkit.common.models import CommonModel

from django.conf import settings

__author__ = 'shade'


def validate_seo_uri(value):

    if not value.startswith('/'):
        raise ValidationError(
            _('uri должен начинаться со слеша'), params={'value': value},
        )

    if settings.APPEND_SLASH and not value.endswith('/'):
        raise ValidationError(
            _('uri должен заканчиваться слешем'), params={'value': value},
        )


class Seo(CommonModel):
    class Meta:
        verbose_name = 'SEO'
        verbose_name_plural = 'SEO'
        unique_together = (('content_type', 'object_id',),)

    title = models.CharField('Meta title', null=True, blank=True, max_length=160)
    description = models.TextField('Meta description', null=True, blank=True)
    keywords = models.TextField('Meta keywords', null=True, blank=True)
    uri = models.CharField('URL без домена', null=True, blank=True, unique=True, db_index=True, max_length=300, validators=[validate_seo_uri])
    uri.help_text = '/ для главной страницы'

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name='Тип объекта', null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey()

    def __str__(self):

        return self.uri
