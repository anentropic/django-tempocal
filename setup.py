# -*- coding: utf-8 -*-
from distutils.core import setup


setup(
    name='django-tempocal',
    version='0.1.2',
    author=u'Anentropic',
    packages=['tempocal'],
    url='https://github.com/anentropic/django-tempocal',
    license='BSD',
    long_description=open('README.rst').read(),
    description=(
        'A django-fied, templated version of Python\'s built-in HTMLCalendar.'
    ),
    zip_safe=False,
    include_package_data=True,
)
