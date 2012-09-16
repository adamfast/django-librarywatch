#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='librarywatch',
    version='1.0.1',
    description='A utility to check PyPi for updates to currently installed packages',
    author='Jeff Triplett / Adam Fast',
    author_email='adamfast@gmail.com',
    url='https://github.com/adamfast/django-librarywatch',
    packages=find_packages(),
    package_data={
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)
