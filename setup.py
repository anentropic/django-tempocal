# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
    name='django-tempocal',
    version='0.1.1',
    author=u'Anentropic',
    packages=find_packages(),
    url='https://github.com/anentropic/django-tempocal',
    license='BSD',
    description='A django-fied, templated version of Python\'s built-in HTMLCalendar.',
    zip_safe=False,
    include_package_data=True,
)