# coding=utf-8
from helpkit.seo.models import Seo

__author__ = 'shade'


def seo(request):

    seo_obj = Seo.objects.filter(uri__in=request.path).first()

    if seo_obj:
        return {'seo': {'title': seo_obj.title,
                        'description': seo_obj.description,
                        'keywords': seo_obj.keywords}}

    return {}
