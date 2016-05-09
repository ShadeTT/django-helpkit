# coding=utf-8

import os
import sys
import datetime
from django.conf import settings
from django.template.context import RequestContext
from django.http.response import HttpResponse
from django.template.loader import render_to_string
from django.utils.six import wraps

__author__ = 'shade'


def pid_lock(*args, **kwargs):

    # TODO: документация

    def outer_wrapper(f):
        filename = kwargs.get('filename')

        def inner_wrapper(*args, **kwargs):

            # TODO: нужна обработка событий ctrl+c и kill

            pid = str(os.getpid())
            pidfile = settings.BASE_DIR + "/%s.pid" % filename

            if os.path.isfile(pidfile):
                sys.exit()
            else:
                file(pidfile, 'w').write(pid)

            try:
                f(*args, **kwargs)
            except:
                pass
            os.unlink(pidfile)

        return inner_wrapper

    return outer_wrapper