# coding=utf-8

from kit import __version__
from setuptools import setup, find_packages

__author__ = 'shade'


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
        'Development Status :: 0.1 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
)