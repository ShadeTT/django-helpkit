# coding=utf-8

import os
from setuptools import find_packages
from setuptools import setup

from helpkit import __version__

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name="django-helpkit",
    version=__version__,
    packages=find_packages(),
    author="El Kolmakov",
    author_email="shdprogrammer@gmail.com",
    license="BSD",
    keywords="django",
    url="https://github.com/ShadeTT/django-helpkit",
    classifiers=[
        'Development Status :: 0.2 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)