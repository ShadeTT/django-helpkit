# coding=utf-8
from django.contrib.contenttypes.models import ContentType
from helpkit.common.models import ImageModel
from helpkit.seo.models import Seo

__author__ = 'shade'


class ContentTypeModelMixin(object):

    @classmethod
    def get_ctype(cls, self=None):

        return self and ContentType.objects.get_for_model(self.__class__) or ContentType.objects.get_for_model(cls)


class ImageMixin(ContentTypeModelMixin, object):

    def images(self):
        return ImageModel.objects.filter(content_type=self.get_ctype(), object_id=self.id)

    def cover_image(self):
        return self.images().first()


class SeoMixin(ContentTypeModelMixin, object):

    @property
    def seo(self):
        return Seo.objects.filter(content_type=self.get_ctype(), object_id=self.id).first()