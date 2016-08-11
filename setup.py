#!/usr/bin/env python
from setuptools import find_packages, setup

EXCLUDE_FROM_PACKAGES = ['tests']

setup(
    name='pgoapi',
    author='tjado',
    description='Pokemon Go API lib',
    version='1.1.6',
    url='https://github.com/tejado/pgoapi',
    download_url='https://github.com/tejado/pgoapi/releases',
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    install_requires=[
        'geopy',
        'gpsoauth',
        'protobuf',
        'requests[socks]',
        's2sphere',
        'six',
        'xxhash',
    ],
)
