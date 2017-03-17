# coding=utf-8

import uuid
import os
from django.core.cache import cache

__author__ = 'shade'


def cached(key, func, ttl=60*60*24):
    data = cache.get(key)
    if data is None:
        data = func()
        cache.set(key, data, ttl)
    return data


def chunked_path(instance, filename):

    """
    make path from filename for FileField upload_to
    example: blabla/f0/a5/64/5e/ee/df/f0a5645eeedf.jpg
    """

    extension = filename.split('.')[-1]

    filename = uuid.uuid4().hex

    fname = list(map(None, *([iter(filename)] * 2)))

    if len(fname) % 2:
        fname[-1] = (fname[-1][0], '')

    fname = map(lambda x: ''.join(x), fname)

    fname.insert(0, instance.__class__.__name__.lower())
    fname.append('%s.%s' % (filename, extension))

    return os.path.join(*fname)
