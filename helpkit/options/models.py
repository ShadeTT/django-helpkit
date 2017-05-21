# coding=utf-8

from django.apps import apps
from django.contrib.sites.models import Site
from django.core.exceptions import AppRegistryNotReady
from django.db import models
from django.db.utils import ProgrammingError, OperationalError

__author__ = 'shade'


class MetaOptions(models.base.ModelBase):

    """
    For easy to use settings(Setting model).
    Instead of Setting.objects.get(name='KEY'), you can use Setting.KEY
    """

    def __getattr__(self, key):

        val = None

        try:
            options = apps.get_model('common', 'CommonOptions')
            option_values = apps.get_model('common', 'OptionValue')
            sites = apps.get_model('sites', 'Site')
        except AppRegistryNotReady:
            pass
        else:
            site = sites.objects.get_current()

            try:
                val = option_values.objects.get(option__name=key).value
            except (OperationalError, options.DoesNotExist, option_values.DoesNotExist, ProgrammingError):
                pass

        return val

    def set_value(self, key, value, value_type=str):

        """
        key = key,
        value = value,
        value_type accept following values:
                unicode
                int
                float

        value_type default - basestring
        """

        options = apps.get_model('common', 'CommonOptions')
        option_values = apps.get_model('common', 'OptionValue')
        sites = apps.get_model('sites', 'Site')

        site = sites.objects.get_current()

        if options.objects.filter(name=key).exists():
            option_values.objects.filter(option__name=key, site=site).update(val=value)

        else:
            option = options.objects.create(name=key, value_type=CommonOptions.VALUE_TYPE_MAPPING.get(value_type))
            val = option_values.objects.create(option_id=option.id, val=value)
            val.site.add(site.id)


class CommonOptions(models.Model, metaclass=MetaOptions):

    """
    Simple project settings
    """

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'
        app_label = 'common'

    VALUE_TYPE_CHOICES = (
        (1, 'Строка',),
        (2, 'Целое',),
        (3, 'Вещественное',),
        (4, 'Rich text',),
        (5, 'Список',),
    )

    VALUE_TYPE_MAPPING = {float: 3, int: 2, str: 1, list: 5}

    VALUE_TYPE_CONVERTER = {
        1: lambda x: str(x),
        2: lambda x: int(x),
        3: lambda x: float(x),
        4: lambda x: str(x),
        5: lambda x: x.split('\r\n'),
    }

    name = models.CharField('Ключ', max_length=100, unique=True)
    value_type = models.PositiveSmallIntegerField('Тип значения', choices=VALUE_TYPE_CHOICES)
    desc = models.TextField('Описание')


class OptionValue(models.Model):

    class Meta:
        verbose_name = 'Значение'
        verbose_name_plural = 'Значения'
        app_label = 'common'

    option = models.ForeignKey(CommonOptions)
    val = models.TextField('Значение')
    site = models.ManyToManyField(Site, verbose_name='Сайт')

    @property
    def value(self):

        return self.option.VALUE_TYPE_CONVERTER[self.option.value_type](self.val)