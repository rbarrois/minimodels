# -*- coding: utf-8 -*-
# Copyright (c) 2013 Raphaël Barrois
# This code is published under the two-clause BSD License

from setuptools import setup, find_packages
import os
import re

root_dir = os.path.abspath(os.path.dirname(__file__))


def get_version(package_name):
    version_re = re.compile(r"^__version__ = [\"']([\w_.-]+)[\"']$")
    package_components = package_name.split('.')
    path_components = package_components + ['__init__.py']
    with open(os.path.join(root_dir, *path_components)) as f:
        for line in f:
            match = version_re.match(line[:-1])
            if match:
                return match.groups()[0]
    return '0.1.0'


PACKAGE = 'minimodel'


setup(
    name="minimodel",
    version=get_version(PACKAGE),
    author="Raphaël Barrois",
    author_email="raphael.barrois+minimodel@polytechnique.org",
    description="A backend-independent database abstraction tool.",
    license="BSD",
    keywords=['model', 'backend', 'abstraction'],
    url="http://github.com/rbarrois/minimodel",
    download_url="http://pypi.python.org/pypi/minimodel/",
    packages=['minimodel'],
    setup_requires=[
        'distribute',
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD",
        "Topic :: Software Development :: Libraries :: Python Modules",
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    test_suite='tests',
)

