# coding=utf-8

import os
import signal
import sys
import tempfile
from django.utils.six import wraps

__author__ = 'shade'


def pid_lock(*args, **kwargs):

    # TODO: документация

    def outer_wrapper(f):

        filename = kwargs.get('filename')

        @wraps(f)
        def inner_wrapper(*args, **kwargs):

            pidfile = os.path.join(tempfile.gettempdir(), "%s.pid" % filename)

            def remove_pid(*args, **kwargs):
                os.remove(pidfile)
                sys.exit()

            signal.signal(signal.SIGINT, remove_pid)

            if os.path.exists(pidfile):

                pid = open(pidfile).read()
                pid = int(pid) if pid else None

                try:
                    os.kill(pid, 0)
                except OSError:
                    os.remove(pidfile)
                except TypeError:
                    os.remove(pidfile)
                else:
                    print 'It is already running'
                    sys.exit()

            pid = str(os.getpid())
            with open(pidfile, 'w') as pf:
                pf.write(pid)

            f(*args, **kwargs)

            os.remove(pidfile)

        return inner_wrapper

    return outer_wrapper